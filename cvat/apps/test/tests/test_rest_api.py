# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from rest_framework import status

from cvat.apps.engine.models import (
    LabeledImage,
    LabeledInterval,
    LabeledShape,
    LabeledTrack,
    Label,
    MediaType,
    ShapeType,
    TaskMode,
    TrackedShape,
)
from cvat.apps.engine.tests.test_rest_api import create_db_task, create_db_users
from cvat.apps.engine.tests.utils import ApiTestBase
from cvat.apps.iam.models import User


class TaskAnnotationCountsAPITest(ApiTestBase):
    @classmethod
    def setUpTestData(cls):
        create_db_users(cls, admin=False, extra=False)
        cls.outsider = User.objects.create_user(username="outsider", password="outsider")
        cls.task = create_db_task(
            {
                "name": "annotation count task",
                "owner": cls.owner,
                "assignee": cls.assignee,
                "overlap": 0,
                "segment_size": 1,
                "image_quality": 75,
                "size": 1,
                "media_type": MediaType.IMAGE,
                "mode": TaskMode.ANNOTATION,
                "labels": [
                    {"name": "person"},
                    {"name": "car"},
                    {"name": "dog"},
                    {"name": "cat"},
                    {"name": "event"},
                    {"name": "unused"},
                ],
            }
        )
        cls.labels = {label.name: label for label in cls.task.label_set.all()}
        cls.labels["person-part"] = Label.objects.create(
            task=cls.task, name="person-part", parent=cls.labels["person"]
        )
        cls.labels["dog-part"] = Label.objects.create(
            task=cls.task, name="dog-part", parent=cls.labels["dog"]
        )
        cls.job = cls.task.segment_set.first().job_set.first()

    def _get_counts(self, user):
        return self._get_request(f"/api/tasks/{self.task.pk}/annotation-counts", user)

    def test_returns_counts_by_class_across_annotation_types_and_elements(self):
        for index in range(2):
            root_shape = LabeledShape.objects.create(
                job=self.job,
                label=self.labels["person"],
                frame=0,
                group=0,
                type=ShapeType.SKELETON if index == 0 else ShapeType.RECTANGLE,
                points=[] if index == 0 else [0, 0, 1, 1],
            )
            if index == 0:
                LabeledShape.objects.create(
                    job=self.job,
                    label=self.labels["person-part"],
                    frame=0,
                    group=0,
                    type=ShapeType.POINTS,
                    points=[0, 0],
                    parent=root_shape,
                )
        LabeledShape.objects.create(
            job=self.job,
            label=self.labels["car"],
            frame=0,
            group=0,
            type=ShapeType.RECTANGLE,
            points=[0, 0, 1, 1],
        )
        track = LabeledTrack.objects.create(
            job=self.job, label=self.labels["dog"], frame=0, group=0
        )
        TrackedShape.objects.create(
            track=track,
            frame=0,
            type=ShapeType.RECTANGLE,
            points=[0, 0, 1, 1],
        )
        child_track = LabeledTrack.objects.create(
            job=self.job,
            label=self.labels["dog-part"],
            frame=0,
            group=0,
            parent=track,
        )
        TrackedShape.objects.create(
            track=child_track,
            frame=0,
            type=ShapeType.POINTS,
            points=[0, 0],
        )
        LabeledImage.objects.create(job=self.job, label=self.labels["cat"], frame=0, group=0)
        LabeledInterval.objects.create(
            job=self.job,
            label=self.labels["event"],
            group=0,
            start=0,
            stop=1,
        )

        response = self._get_counts(self.owner)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "person": 2,
                "person-part": 1,
                "car": 1,
                "dog": 1,
                "dog-part": 1,
                "cat": 1,
                "event": 1,
            },
        )

    def test_omits_classes_without_annotations(self):
        LabeledShape.objects.create(
            job=self.job,
            label=self.labels["person"],
            frame=0,
            group=0,
            type=ShapeType.RECTANGLE,
            points=[0, 0, 1, 1],
        )

        response = self._get_counts(self.owner)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"person": 1})
        self.assertNotIn("unused", response.data)

    def test_nonexistent_task_returns_not_found(self):
        response = self._get_request("/api/tasks/999999/annotation-counts", self.owner)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authentication_and_task_permissions(self):
        response = self._get_counts(None)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self._get_counts(self.outsider)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self._get_counts(self.owner)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
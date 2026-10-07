# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from cvat.apps.engine import models
from cvat.apps.engine.permissions import TaskPermission


class TaskAnnotationCountsViewSet(viewsets.GenericViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.Serializer
    filter_backends = ()
    iam_permission_class = TaskPermission
    iam_supports_organization_params = True

    def annotations(self, request, pk=None):
        task = self.get_object()
        counts = {}

        for annotation_model in (
            models.LabeledImage,
            models.LabeledShape,
            models.LabeledTrack,
            models.LabeledInterval,
        ):
            annotations = annotation_model.objects.filter(job__segment__task_id=task.pk)

            for result in annotations.values("label__name").annotate(count=Count("pk")):
                label_name = result["label__name"]
                counts[label_name] = counts.get(label_name, 0) + result["count"]

        return Response(counts)
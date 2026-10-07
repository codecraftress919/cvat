# Plan

## Goal

Deliver a task-level annotation-count API grouped by class and a task-level Annotation Analytics page with a bar chart.

## Implementation approach

1. Review CVAT's existing task API, annotation data model, and permission checks.
2. Implement backend aggregation in `cvat/apps/test/` and expose counts by class through `GET /api/tasks/<task_id>/annotation-counts`.
3. Add automated API tests for count correctness and relevant empty-data and access cases.
4. Build the task-level Annotation Analytics page using CVAT's existing frontend patterns and chart library.
5. Verify the endpoint and page against a live CVAT instance; measure authenticated API response time across five runs and document the results.

# Objectives

- **API delivery and correctness:** Provide the task annotation-count API grouped by class. Confirm counts against known task annotations; four backend automated tests pass with zero failures and zero errors.
- **Frontend analytics:** Provide a task-level Annotation Analytics page with a bar chart that identifies each class and its annotation count.
- **Live verification:** Verify the endpoint and analytics page against the running CVAT instance using Task #3, COCO 2017 validation, with 5,000 frames.
- **Performance:** Across five authenticated API runs on the test machine, achieve a median response time below 1 second. This is a local acceptance target, not a production SLA.

## Measurement Conditions

- OS: Microsoft Windows 11 Pro 10.0.26200
- CPU: AMD Ryzen 7 7735U with Radeon Graphics
- CPU cores / logical processors: 8 / 16
- Total RAM: approximately 15.28 GiB
- Free RAM at measurement: approximately 3.61 GiB
- Baseline CVAT commit SHA: `c4f0c2a54dd7d95bc222836c645e8c290858fd05`
- Test task: Task #3, COCO 2017 validation, 5,000 frames
- Request: authenticated `GET /api/tasks/3/annotation-counts` against the running CVAT instance

## Performance Results

Authenticated response times:

| Run | Response time |
| --- | ---: |
| 1 | 77.67 ms |
| 2 | 71.30 ms |
| 3 | 71.17 ms |
| 4 | 68.57 ms |
| 5 | 67.39 ms |

- Median: 71.17 ms
- Minimum: 67.39 ms
- Maximum: 77.67 ms
- Spread (maximum − minimum): 10.28 ms
- Local acceptance target: median below 1 second; met. This target is not a production SLA.

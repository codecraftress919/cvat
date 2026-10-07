# Objectives

- Deliver a documented task-level API that reports annotation counts grouped by class.
- Demonstrate correctness with API tests that compare returned counts against known annotations, including an empty task and permission checks.
- Verify the endpoint against a running CVAT instance and record the observed response and measurement conditions.

## Measurement Conditions

- OS: Microsoft Windows 11 Pro 10.0.26200
- CPU: AMD Ryzen 7 7735U with Radeon Graphics
- CPU cores / logical processors: 8 / 16
- Total RAM: approximately 15.28 GiB
- Free RAM at measurement: approximately 3.61 GiB
- CVAT commit SHA: ef3c26b459fde1363a3d2dc3e9c285a0b273e1ab
- Test task: Task #3, COCO 2017 validation, 5,000 frames
- Endpoint: GET /api/tasks/3/annotation-counts
- Verification: Endpoint returned annotation counts successfully from the running CVAT instance while authenticated in the browser.
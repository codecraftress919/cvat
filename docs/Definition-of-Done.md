# Definition of Done

- **Backend:** The task-level API in `cvat/apps/test/` returns annotation counts grouped by class and respects task access permissions.
- **Frontend:** A task-level Annotation Analytics page shows the returned class counts in a bar chart and handles loading, empty data, and API failure states.
- **Automated tests:** Backend API tests pass; recorded result is 4 tests, 0 failures, 0 errors.
- **Documentation:** Endpoint, implementation scope, verification conditions, and measured results are recorded in the assessment documents.
- **Live verification:** The API and page work against the running CVAT instance for Task #3 (COCO 2017 validation, 5,000 frames).
- **Measurements:** Record five authenticated API runs: 77.67, 71.30, 71.17, 68.57, and 67.39 ms; median 71.17 ms; spread 10.28 ms. The local acceptance target is a median below 1 second and is not a production SLA.
- **Git/PR:** Review the final diff, commit the completed changes, and open or update a pull request with a summary and verification evidence.
- **Loom:** Provide a Loom recording showing the live analytics page and API verification.

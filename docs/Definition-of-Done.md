# Definition of Done

- **Implementation:** The task annotation-count API follows existing routing, response, and task-permission conventions and has defined count semantics.
- **Tests:** Automated tests cover count accuracy, empty data, applicable annotation types, and authorization or access denial.
- **Documentation:** The API endpoint, response fields, count semantics, and verification steps are documented.
- **Live verification:** Exercise the endpoint against a running CVAT instance with representative annotated and empty tasks; capture the observed responses.
- **Measurements:** Record measured results and the environment or conditions used. Report observations as measured and do not substitute invented targets or values.
- **Git/PR:** Review the final diff, commit the completed changes, and open or update a pull request with a concise summary and verification evidence.
- **Loom:** Provide a Loom recording demonstrating the endpoint in the running application and summarizing the implementation and verification.

# Plan

## Goal

Add annotation analytics to CVAT that shows the number
of annotations per class for a task.

## Order of Work

1. Set up CVAT locally with Docker.
2. Import COCO validation dataset.
3. Create Django app named test.
4. Implement API for annotation counts by class.
5. Add authentication and task permission checks.
6. Build frontend analytics page.
7. Display counts using a graph.
8. Handle empty data and failed requests.
9. Measure API performance.
10. Add one useful filter/grouping.
11. If time allows, add WebSocket live updates and reconnect handling.

## Time Allocation

- Setup: 45 minutes
- Documentation and exploration: 30 minutes
- Backend API: 1.5 hours
- Authentication/permissions: 45 minutes
- Frontend: 1 hour
- Graph and states: 45 minutes
- Performance measurement: 30 minutes
- Filter/grouping: 30 minutes
- WebSocket: remaining time
- Testing/documentation/recording: remaining time

## Initially Skipped

WebSocket live updates will be attempted only after
the core requirements are complete.

## Decision Record

I will keep the analytics logic in the backend because
the requirement is to read annotation counts from the
database and expose them through an API.
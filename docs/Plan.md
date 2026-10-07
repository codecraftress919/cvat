# Plan

## Goal

Provide a task-level API that returns annotation counts grouped by class, using CVAT's existing task data and permission model.

## Implementation approach

1. Review the task annotation API, annotation data model, and existing task permissions to align with established patterns.
2. Define a read-only task endpoint and response schema for per-class counts. Specify which annotation types are counted and how classes with zero annotations are represented.
3. Aggregate counts server-side from the task's annotations, avoiding full annotation serialization where practical.
4. Apply the existing task access checks and return standard API errors for missing tasks or unauthorized requests.
5. Add focused API tests for count accuracy, relevant annotation types, empty annotations, and permission behavior.
6. Document the endpoint and its response, then verify it against a live CVAT instance and record measured results without setting an assumed performance target.

## Scope

This work covers the task annotation-count API and its tests and documentation. UI analytics and live updates are outside this plan.

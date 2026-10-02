# Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Usability | The interface must be simple enough for a writer to submit an article without training. Navigation between Writer and Reviewer views must be intuitive. |
| NFR-02 | Reliability | The system must not crash on invalid input. All user errors must result in a clear feedback message, not a system exception. |
| NFR-03 | Maintainability | Code must follow standard Python/Flask conventions. Project structure must be clean and documented so that future weeks can build upon it. |
| NFR-04 | Testability | The application must expose clean HTTP endpoints and use identifiable HTML element IDs so that Selenium can predictably locate and test UI elements. |
| NFR-05 | Performance | The MVP must respond to user actions within a reasonable time on a local development machine. No specific response-time SLA is required for an academic project. |
| NFR-06 | Portability | The application must run on Windows and Linux environments. SQLite (file-based) and Python ensure no platform-specific dependencies. |
| NFR-07 | Deployment Consistency | The application must run identically in the local development environment and inside a Docker container. Configuration must not be hardcoded. |
| NFR-08 | Error Handling | The UI must display user-friendly error messages. System stack traces must not be shown to the end user. |
| NFR-09 | Logging | Basic HTTP request logging must be output to standard output (stdout) so that Jenkins and Docker can capture logs. |
| NFR-10 | Security | SQL injection prevention via parameterized queries. Authentication and RBAC are explicitly excluded from MVP scope. |

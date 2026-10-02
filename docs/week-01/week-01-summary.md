# Week 1 Summary: Problem Definition and Scope

### Problem
Manual application deployments are slow and error-prone due to a lack of automated CI/CD and configuration management.

### Users
- News Writers (Submit articles)
- Reviewers / Editors (Review, approve, or reject articles)

### Stakeholders
- Development & Operations Team (Student)
- Academic Evaluators / Instructors

### Pain Points
Manual coordination, lack of automated validation, manual deployment configurations, and inconsistent environments.

### Objectives
- **Application:** Build a simple, monolithic News Publishing Workflow.
- **DevOps:** Implement a complete, automated CI/CD pipeline and infrastructure provisioning system.

### Constraints
- 15-week academic timeline.
- Application must remain a simple monolith; no microservices.
- Technologies to be decided in Week 3.

### Success Criteria
- **Application:** Submission, approval/rejection, and status tracking work correctly.
- **DevOps:** A successful code change should be able to pass through automated build, testing and deployment stages in Jenkins with deployment blocked when automated tests fail. Infrastructure can be provisioned from scratch via Ansible/Puppet.

### MVP Scope
- Article/request submission
- Required-field validation
- Reviewer dashboard
- Reviewer approval
- Reviewer rejection with mandatory comment
- Status tracking

### Out-of-Scope Features
- Authentication, RBAC, payments, AI, social media, real-time feeds, microservices, Kubernetes.

### Assumptions
- Target deployment environment may be local.
- Roles will be simulated/mocked instead of using secure authentication.

### Week 1 Conclusion
The project scope has been clearly defined with a strict boundary on application complexity to ensure the focus remains on DevOps practices. The requirements, users, and high-level success criteria are established, setting the foundation for agile planning in Week 2.

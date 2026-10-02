# MVP Scope

## 1. MVP Purpose
The News Publishing Workflow application is intentionally small. The primary academic objective is to demonstrate the progressive implementation of DevOps practices rather than to develop a full-scale news portal.

## 2. Application MVP Features
The application MVP must contain **ONLY**:
- News article/request submission
- Required-field/data validation
- Reviewer dashboard
- Reviewer approval
- Reviewer rejection with mandatory rejection comment
- Article status tracking

## 3. DevOps Scope
- **Version Control:** Git and GitHub for source code management.
- **Continuous Integration (CI):** Jenkins to automate builds.
- **Continuous Testing:** Automated Selenium testing integrated into Jenkins.
- **Containerization:** Docker for packaging the application.
- **Continuous Deployment (CD):** Jenkins-Docker integration for automated deployment.
- **Configuration Management:** Ansible or Puppet for server provisioning.

## 4. In-Scope Items
- Basic monolithic frontend and backend application.
- Basic role simulation/mocking to switch between Writer and Reviewer views.
- Local or academically provided deployment environment.

## 5. Explicitly Out-of-Scope Items
- User authentication and role-based access control (RBAC).
- Payment gateways or subscriptions.
- AI news generation or recommendation systems.
- Social media integrations, comments, or likes.
- Real-time news feeds or complex UI animations.
- Large-scale microservices architecture or Kubernetes.
- Analytics or notifications.

## 6. Constraints
- Strictly limited to a 15-week academic schedule.
- The application must be a simple, monolithic application. Microservices will not be used.
- The programming language, framework, and database are not finalized in Week 1 and will be determined during Week 3 based on project requirements.

## 7. Assumptions
- A local or academically provided environment will be available to host Jenkins, Docker, and target deployment servers (not necessarily cloud-based).
- Testing data and scenarios will be synthetic and predefined.

## 8. MVP Boundaries
The application is strictly limited to the submission and review workflow to ensure the majority of project time is spent on DevOps implementation, pipeline orchestration, and configuration management.

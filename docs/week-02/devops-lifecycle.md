# DevOps Lifecycle

The DevOps lifecycle for the News Publishing Workflow project ensures continuous integration, continuous delivery, and high quality throughout the 15 weeks.

| Stage | Context for this Project | Planned Tools |
|---|---|---|
| **PLAN** | Defining MVP scope, Agile planning, generating the backlog. | Markdown, Agile Task Boards |
| **CODE** | Developing the monolithic application logic (Writer/Reviewer views). | Git, GitHub |
| **BUILD** | Compiling the application and resolving dependencies automatically. | Jenkins, (Build tool TBD in Week 3) |
| **TEST** | Running automated validation on the UI to prevent bugs. | Jenkins, Selenium |
| **RELEASE** | Tagging code, packaging the application into a container. | Git, Docker |
| **DEPLOY** | Pushing the container to the target server environment. | Jenkins, Docker |
| **OPERATE** | Provisioning and maintaining server configurations via code. | Ansible/Puppet |
| **MONITOR / FEEDBACK** | Checking if the application is accessible and reviewing pipeline status. | Jenkins |

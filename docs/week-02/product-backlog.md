# Product Backlog

| ID | Task / User Story | Type | Priority | Week | Dependencies | Completion Condition | Est. Effort |
|---|---|---|---|---|---|---|---|
| **B-01** | Define problem, stakeholders, scope | Doc | High | 1 | None | Week 1 Docs Approved | 1 wk |
| **B-02** | Agile Planning & Workflow | Doc | High | 2 | B-01 | Week 2 Docs Approved | 1 wk |
| **B-03** | Architecture & Tech Stack Setup | Tech | High | 3 | B-02 | Tech Stack Selected | 1 wk |
| **B-04** | Initialize Git/GitHub Repository | DevOps | High | 4 | B-03 | Repo Accessible | 1 wk |
| **B-05** | Develop submission/validation | App | High | 5 | B-04 | US-01,02,03,04 Pass | 1 wk |
| **B-06** | Develop review dashboard | App | High | 6 | B-05 | US-05,06,07,08,09 Pass | 1 wk |
| **B-07** | Install Jenkins & Config Job | DevOps | High | 7 | B-06 | Trigger on Commit | 1 wk |
| **B-08** | Convert to Pipeline as Code | DevOps | High | 8 | B-07 | Jenkinsfile works | 1 wk |
| **B-09** | Design Selenium UI tests | App/Test | High | 9 | B-06 | Scripts pass locally | 1 wk |
| **B-10** | Integrate Selenium in Jenkins | DevOps | High | 10 | B-08, B-09 | Tests run on CI | 1 wk |
| **B-11** | Create Dockerfile | DevOps | High | 11 | B-06 | Image builds locally | 1 wk |
| **B-12** | Jenkins-Docker CD Pipeline | DevOps | High | 12 | B-10, B-11 | CI deploys container | 1 wk |
| **B-13** | Write Ansible/Puppet scripts | DevOps | High | 13 | B-12 | Scripts execute | 1 wk |
| **B-14** | Automate Provisioning in CD | DevOps | High | 14 | B-13 | End-to-End Success | 1 wk |
| **B-15** | Final Release & Documentation | Doc | High | 15 | B-14 | Viva Completed | 1 wk |

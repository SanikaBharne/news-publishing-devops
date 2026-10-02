# Jenkins Installation Documentation

## Overview
Jenkins is an open-source automation server used to implement Continuous Integration (CI) in this project. This document outlines the Jenkins installation and initial setup steps performed during Week 7.

## Installation Steps
1. **Download**: Downloaded the Jenkins Long-Term Support (LTS) installer for Windows.
2. **Execution**: Ran the Jenkins installer (`jenkins.msi`).
3. **Service Configuration**: Configured Jenkins to run as a local or network service as appropriate for the development machine.
4. **Port Configuration**: Jenkins was configured to run on the default port `8080`.
5. **Java Dependency**: Ensure an appropriate Java Development Kit (JDK 17 or 21) was installed and added to the environment variables, as Jenkins requires Java to run.

## Initial Setup
1. **Unlock Jenkins**: Navigated to `http://localhost:8080` in the browser. Retrieved the initial administrator password from `C:\ProgramData\Jenkins\.jenkins\secrets\initialAdminPassword`.
2. **Plugin Installation**: Selected "Install suggested plugins". This installs the base set of plugins, including Git and Pipeline plugins required for this project.
3. **Admin User**: Created the first admin user account to secure the Jenkins instance.
4. **Instance Configuration**: Confirmed the Jenkins URL (`http://localhost:8080/`).

## Verification
Jenkins is now accessible and fully operational at `http://localhost:8080/`. The dashboard shows the Welcome screen, ready for pipeline creation.

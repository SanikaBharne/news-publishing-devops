pipeline {
    agent any

    tools {
        maven 'Maven-3.9.16'
    }

    options {
        disableConcurrentBuilds()
    }

    environment {
        DEPLOY_HOST = "127.0.0.1"
        DEPLOY_PORT = "5016"
        CONTAINER_NAME = "newsflow-week15-staging"
        DATABASE_VOLUME = "newsflow-week15-staging-data"
        IMAGE_NAME = "news-publishing-app"
        IMAGE_TAG = "week15-staging"
        APP_BASE_URL = "http://127.0.0.1:5016"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Checked out ${env.GIT_BRANCH ?: 'configured SCM branch'}."
            }
        }

        stage('Check Python') {
            steps {
                bat '''
                    where.exe python
                    python --version
                    python -m pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    if errorlevel 1 exit /b 1
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if errorlevel 1 exit /b 1
                    pip install -r requirements.txt
                    if errorlevel 1 exit /b 1
                """
            }
        }

        stage('Maven Validation') {
            steps {
                bat """
                    where.exe mvn
                    if errorlevel 1 exit /b 1
                    mvn --batch-mode validate
                    if errorlevel 1 exit /b 1
                """
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if errorlevel 1 exit /b 1
                    python -m pytest tests\\test_submission.py tests\\test_reviewer.py tests\\test_auth_public.py -v
                    if errorlevel 1 exit /b 1
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                    powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\\verify_docker_engine.ps1
                    if errorlevel 1 exit /b 1
                    docker build -t %IMAGE_NAME%:%IMAGE_TAG% -t %IMAGE_NAME%:%IMAGE_TAG%-build-%BUILD_NUMBER% .
                    if errorlevel 1 exit /b 1
                """
            }
        }

        stage('Deploy Docker Container') {
            steps {
                bat """
                    powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\\deploy_docker.ps1 -Image "%IMAGE_NAME%:%IMAGE_TAG%-build-%BUILD_NUMBER%" -ContainerName "%CONTAINER_NAME%" -VolumeName "%DATABASE_VOLUME%" -HostPort %DEPLOY_PORT% -BuildId "%BUILD_NUMBER%"
                """
            }
        }

        stage('Health Check') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if errorlevel 1 exit /b 1
                    python scripts\\healthcheck.py %DEPLOY_HOST% %DEPLOY_PORT% 20
                    if errorlevel 1 exit /b 1
                    powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\\verify_container.ps1 -ContainerName "%CONTAINER_NAME%"
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if errorlevel 1 exit /b 1
                    echo Deployment smoke check target: %APP_BASE_URL% (checked in Health Check stage)
                    echo Selenium starts an isolated temporary application; its actual URL is printed by the fixture.
                    python -m pytest tests\\selenium -v
                    if errorlevel 1 exit /b 1
                """
            }
        }

        stage('Final Verification') {
            steps {
                bat """
                    powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\\verify_container.ps1 -ContainerName "%CONTAINER_NAME%"
                    if errorlevel 1 exit /b 1
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if errorlevel 1 exit /b 1
                    python scripts\\healthcheck.py %DEPLOY_HOST% %DEPLOY_PORT% 3
                    if errorlevel 1 exit /b 1
                    echo Deployed image: %IMAGE_NAME%:%IMAGE_TAG%-build-%BUILD_NUMBER%
                    echo Running container: %CONTAINER_NAME%
                    echo Application URL: %APP_BASE_URL%
                """
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Collecting logs from the named application container when it exists."
            script {
                bat(returnStatus: true, script: 'powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\\diagnose_container.ps1 -ContainerName newsflow-week15-staging')
                bat(returnStatus: true, script: 'docker ps -a --filter "name=^newsflow-week15-staging$"')
            }
        }
        always {
            echo "Pipeline finished. The successfully deployed application container is intentionally left running."
        }
        success {
            echo "Pipeline succeeded: Docker deployment is healthy and Selenium tests passed."
        }
    }
}

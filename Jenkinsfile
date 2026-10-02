pipeline {
    agent any

    environment {
        DEPLOY_PORT = "5001"
        DEPLOY_HOST = "127.0.0.1"
        VENV_DIR   = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo "Source code checked out."
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pip install -r requirements.txt
                """
                echo "Dependencies installed."
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python -m pytest -v
                """
            }
        }

        stage('Deploy Application') {
            steps {
                // Gunicorn is the standard WSGI server for Flask on Linux/production.
                // On Windows (where this Jenkins agent runs), gunicorn is unavailable
                // (requires the POSIX fcntl module). The Windows-compatible equivalent
                // is 'waitress', which is included in requirements.txt alongside gunicorn.
                // scripts/deploy.py uses waitress to serve the app on port 5001.
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    echo Stopping any previous instance on port %DEPLOY_PORT%...
                    for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":%DEPLOY_PORT% " ^| findstr LISTENING') do (
                        taskkill /PID %%p /F 2>nul || echo No process to kill.
                    )
                    echo Starting application on %DEPLOY_HOST%:%DEPLOY_PORT% ...
                    start /B python scripts\\deploy.py
                    echo Deployment started (background process).
                """
                // Allow the server a few seconds to come up before health check
                sleep time: 8, unit: 'SECONDS'
            }
        }

        stage('Health Check') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python scripts\\healthcheck.py %DEPLOY_HOST% %DEPLOY_PORT% 10
                """
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
            // Attempt to stop the deployment process when the pipeline ends
            bat """
                for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":%DEPLOY_PORT% " ^| findstr LISTENING 2^>nul') do (
                    taskkill /PID %%p /F 2>nul || echo No deployment process to stop.
                )
            """
        }
        success {
            echo "Pipeline succeeded! All tests passed and health check OK on port ${DEPLOY_PORT}."
        }
        failure {
            echo "Pipeline failed! Check logs above for the failing stage."
        }
    }
}

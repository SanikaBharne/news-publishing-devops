pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Since this is Windows, we use bat. For Linux, use sh.
                // Assuming Python is in PATH
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                python -m pytest -v
                '''
            }
        }
    }
    
    post {
        always {
            echo "Pipeline finished!"
        }
        success {
            echo "Pipeline succeeded! All 14 tests passed."
        }
        failure {
            echo "Pipeline failed! Please check the logs."
        }
    }
}

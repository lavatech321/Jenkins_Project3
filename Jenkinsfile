pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }
        stage('Analyse') {
          steps {
            sh 'python3 analyse.py'
          }
        }
    }
}

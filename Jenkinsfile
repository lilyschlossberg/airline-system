pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'lilyschlossberg/airline-system'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '/Applications/miniconda3/bin/pip3 install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh '/Applications/miniconda3/bin/flake8 app/'
            }
        }

        stage('Test') {
            steps {
                sh '/Applications/miniconda3/bin/pytest tests/ --cov=app || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t lilyschlossberg/airline-system .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-creds', url: '' ]) {
                    sh 'docker push lilyschlossberg/airline-system'
                }
            }
        }
    }
}

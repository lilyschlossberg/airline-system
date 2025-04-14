pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'lilyschlossberg/airline-system'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 app/'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/ --cov=app || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_REPO}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-creds', url: '' ]) {
                    script {
                        docker.image("${DOCKER_HUB_REPO}").push('latest')
                    }
                }
            }
        }
    }
}

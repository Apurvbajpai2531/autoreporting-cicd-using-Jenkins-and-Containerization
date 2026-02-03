pipeline {
    agent any

    stages() {
        stage("Coding section") {
            steps {
                git branch: 'main',
                    url: 'git@github.com:Apurvbajpai2531/autoreporting-cicd-using-Jenkins-and-Containerization.git'
            }
        }

        stage("Build Container") {
            steps {
                sh '''
                docker compose build
                '''
            }
        }

        stage('Deploy Services') {
            steps {
                sh '''
                docker compose down || true
                docker compose up -d
                '''
            }
        }
    }
}

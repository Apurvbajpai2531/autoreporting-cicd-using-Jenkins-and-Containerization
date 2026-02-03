pipeline {
    agent any

    stages() {
        stage("Coding section") {
            steps {
                git branch: 'main',
                      url: 'https://github.com/Apurvbajpai2531/autoreporting-cicd-using-Jenkins-and-Containerization.git',
    credentialsId: 'github-pat'
            }
        }

       stage("Build Container") {
    steps {
        sh '''
        docker compose version
        docker compose build
        '''
    }
}

stage('Deploy Services') {
    steps {
        sh '''
        docker compose down || true
        docker compose up -d
        docker ps
        '''
    }
}
    }
}

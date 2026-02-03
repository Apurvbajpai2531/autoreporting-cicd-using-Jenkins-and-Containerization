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
        /usr/bin/docker compose build
        '''
    }
}

stage('Deploy Services') {
    steps {
        sh '''
        /usr/bin/docker compose down || true
        /usr/bin/docker compose up -d
        /usr/bin/docker ps
        '''
    }
}

    }
}

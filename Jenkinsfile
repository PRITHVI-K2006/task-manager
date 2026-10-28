pipeline {
    agent any
    environment {
        IMAGE = "prithivi2006/task-manager"
        TAG = "${env.BRANCH_NAME}"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build Image') {
            steps { bat "docker build -t %IMAGE%:%TAG% ." }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    bat "echo %DH_PASS%| docker login -u %DH_USER% --password-stdin"
                    bat "docker push %IMAGE%:%TAG%"
                }
            }
        }
    }
}
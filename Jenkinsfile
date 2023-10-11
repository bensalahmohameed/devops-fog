pipeline {
    agent any// No 'agent none' here since you want to run stages on specific nodes

    stages {
        stage('edge1') {
            agent {
                label 'edge1' // Specify the label of the node you want to run this stage on
            }
            steps {
                sh "git config --global user.name 'bensalahmohameed'"
                sh "git config --global user.email 'salih@yahoo.com'"
                sh 'git pull'
                sh 'python3 encrypt1.py'
                // Add more build steps specific to the 'edge1' node here
            }
        }
        stage('edge2') {
            agent {
                label 'edge2' // Specify the label of the node you want to run this stage on
            }
            steps {
                sh "git config --global user.name 'bensalahmohameed'"
                sh "git config --global user.email 'salih@yahoo.com'"
                sh 'git pull'
                sh 'python3 encrypt2.py'
                // Add more build steps specific to the 'edge2' node here
            }
        }
    }
}

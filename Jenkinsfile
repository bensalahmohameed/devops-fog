pipeline {
    // No 'agent none' here since you want to run stages on specific nodes

    stages {
        stage('edge1') {
            agent {
                label 'edge1' // Specify the label of the node you want to run this stage on
            }
            steps {
                sh 'git pull'
                sh 'touch edge1file'
                sh 'git add edge1file'
                sh "git commit -m 'edge1file added from Jenkins'"
                sh 'git push'
                // Add more build steps specific to the 'edge1' node here
            }
        }
        stage('edge2') {
            agent {
                label 'edge2' // Specify the label of the node you want to run this stage on
            }
            steps {
                sh 'git pull'
                sh 'touch edge2file'
                sh 'git add edge2file'
                sh "git commit -m 'edge2file added from Jenkins'"
                sh 'git push'
                // Add more build steps specific to the 'edge2' node here
            }
        }
    }
}

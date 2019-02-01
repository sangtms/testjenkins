pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                hipchatSend color: 'YELLOW', credentialId: '54240709b1209a59b50b344d707ce4', message: '[STARTED] ' + env.BRANCH_NAME + ' $JOB_NAME #$BUILD_NUMBER ($HIPCHAT_CHANGES_OR_CAUSE) ($COMMIT_MESSAGE) (<a href="$BLUE_OCEAN_URL">View detail</a>)'
                bat 'python -u deploy.py ' + env.BRANCH_NAME
            }
        }
    }
    post {
        always {
            echo 'Just for test'
        }
        success {
            hipchatSend color: 'GREEN', credentialId: '54240709b1209a59b50b344d707ce4', message: '[SUCCESS] $JOB_NAME #$BUILD_NUMBER after $BUILD_DURATION (<a href="$BLUE_OCEAN_URL">View detail</a>)'
        }
        failure {
            hipchatSend color: 'RED', credentialId: '54240709b1209a59b50b344d707ce4', message: '[FAILED] $JOB_NAME #$BUILD_NUMBER after $BUILD_DURATION (<a href="$BLUE_OCEAN_URL">View detail</a>)'
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {			
                bat 'python -u mattermost.py ' + '[STARTED] ' + env.BRANCH_NAME + ' $JOB_NAME #$BUILD_NUMBER ($HIPCHAT_CHANGES_OR_CAUSE) ($COMMIT_MESSAGE) (<a href="$BLUE_OCEAN_URL">View detail</a>)'
				bat 'python -u deploy.py ' + env.BRANCH_NAME
            }
        }
    }
    post {
        always {
            echo 'Just for test (SangTM)'
        }
        success {
			bat 'python mattermost.py ' + '[SUCCESS] $JOB_NAME #$BUILD_NUMBER after $BUILD_DURATION (<a href="$BLUE_OCEAN_URL">View detail</a>)'
        }
        failure {
			bat 'python mattermost.py ' + '[FAILED] $JOB_NAME #$BUILD_NUMBER after $BUILD_DURATION (<a href="$BLUE_OCEAN_URL">View detail</a>)'
        }
    }
}
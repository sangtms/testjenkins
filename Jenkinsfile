pipeline {
    agent any
    stages {
        stage('Build') {
            steps {			
				def message = '[STARTED] ' + env.BRANCH_NAME + ' $JOB_NAME #$BUILD_NUMBER ($HIPCHAT_CHANGES_OR_CAUSE) ($COMMIT_MESSAGE) (<a href="$BLUE_OCEAN_URL">View detail</a>)'
                bat 'python -u mattermost.py ' + message
				bat 'python -u deploy.py ' + env.BRANCH_NAME
            }
        }
    }
    post {
        always {
            echo 'Just for test (SangTM)'
        }
        success {
			def message = '[SUCCESS] $JOB_NAME #$BUILD_NUMBER after $BUILD_DURATION (<a href="$BLUE_OCEAN_URL">View detail</a>)'
			bat 'python mattermost.py ' + message
        }
        failure {
			def message = '[FAILED] $JOB_NAME #$BUILD_NUMBER after $BUILD_DURATION (<a href="$BLUE_OCEAN_URL">View detail</a>)'
			bat 'python mattermost.py ' + message
        }
    }
}
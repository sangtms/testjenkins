pipeline {
    agent any
    stages {
        stage('Build') {
            steps {			
                //bat 'python mattermost.py [STARTED] ' + env.BRANCH_NAME + ' ${JOB_NAME} #${BUILD_NUMBER} (${HIPCHAT_CHANGES_OR_CAUSE}) (${COMMIT_MESSAGE}) (<a href="${BLUE_OCEAN_URL}">View detail</a>)'
				bat 'python mattermost.py [STARTED] ' + env.BRANCH_NAME + ' ' + env.JOB_NAME + ' #' + env.BUILD_NUMBER + ' (' + env.HIPCHAT_CHANGES_OR_CAUSE+ ') (' + env.COMMIT_MESSAGE + ') [View detail](' + env.BLUE_OCEAN_URL + ')'
				bat 'python deploy.py ' + env.BRANCH_NAME
            }
        }
    }
    post {
        always {
            echo 'Just for test (SangTM)'
        }
        success {
			//bat 'python mattermost.py [SUCCESS] ${JOB_NAME} #${BUILD_NUMBER} after ${BUILD_DURATION} (<a href="${BLUE_OCEAN_URL}">View detail</a>)'
			bat 'python mattermost.py [SUCCESS] ' + env.JOB_NAME + ' #' + env.BUILD_NUMBER + ' after ' + env.BUILD_DURATION + ' [View detail](' + env.BLUE_OCEAN_URL + ')'
        }
        failure {
			//bat 'python mattermost.py [FAILED] ${JOB_NAME} #${BUILD_NUMBER} after ${BUILD_DURATION} (<a href="${BLUE_OCEAN_URL}">View detail</a>)'
			bat 'python mattermost.py [FAILED] ' + env.JOB_NAME + ' #' + env.BUILD_NUMBER + ' after ' + env.BUILD_DURATION + ' [View detail](' + env.BLUE_OCEAN_URL + ')'
        }
    }
}
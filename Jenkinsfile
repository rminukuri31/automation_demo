pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'qa', 'stg', 'prod'],
            description: 'Target environment'
        )
        string(
            name: 'JDBC_URL',
            description: 'JDBC URL for selected environment'
        )
    }

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Validate Inputs') {
            steps {
                script {
                    if (!params.JDBC_URL?.trim()) {
                        error "JDBC_URL must be provided"
                    }
                }
            }
        }

        stage('Setup Python venv') {
            steps {
                sh '''
                    python3 -m venv automation.venv
                    . automation.venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Update JDBC Config (Python)') {
            steps {
                sh '''
                    . automation.venv/bin/activate
                    ENV=${ENV} JDBC_URL=${JDBC_URL} python scripts/update_jdbc.py
                '''
            }
        }

        stage('Commit Config Changes to Git') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'Automation_github_token',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_TOKEN'
                )]) {
                    sh '''
                        git config user.email "jenkins@automation.com"
                        git config user.name "jenkins-bot"

                        git add configs/${ENV}/app.properties
                        git commit -m "Update JDBC config for ${ENV} - build ${BUILD_NUMBER}" || echo "No changes to commit"

                        git push https://${GIT_USER}:${GIT_TOKEN}@github.com/rminukuri31/automation_demo.git main
                    '''
                }
            }
        }

        stage('Deploy Config (Ansible)') {
            steps {
                sh '''
                    ENV=${ENV} ansible-playbook -i inventory playbook.yml
                '''
            }
        }
    }

    post {
        success {
            echo "Deployment successful for ${ENV}"
        }
        failure {
            echo "Deployment failed for ${ENV}. Check Jenkins logs and Git history."
        }
    }
}

pipeline {
    agent any

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

        stage('Update JDBC Config (Python)') {
            steps {
                sh '''
                    source automation.venv/bin/activate
                    ENV=${ENV} JDBC_URL=${JDBC_URL} python scripts/update_jdbc.py
                '''
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
}
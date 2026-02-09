JDBC Configuration Automation Demo
This project demonstrates an end-to-end DevOps automation for updating and deploying environment-specific JDBC configurations using Python, Ansible, Git, and Jenkins.
The goal is to simulate a real-world CI/CD-driven configuration update workflow and eliminate manual config changes.

What This Demo Does

Updates JDBC URLs dynamically per Environment
Validates inputs before making changes
Deploys updated configs using Ansible
Orchestrates everything through a Jenkins pipeline

Tools & Technologies

Python 3 – configuration update logic
Ansible – deployment automation
Jenkins – CI/CD orchestration
Git & GitHub – version control
Linux / WSL – execution environment

Project Structure
automation_demo/
├── scripts/
│   └── update_jdbc.py        # Python script to update JDBC config
├── configs/
│   ├── dev/app.properties
│   ├── qa/app.properties
│   ├── stg/app.properties
│   └── prod/app.properties
├── playbook.yml              # Ansible playbook
├── inventory                 # Ansible inventory
├── requirements.txt          # Python dependencies
├── Jenkinsfile               # Jenkins pipeline definition
├── .gitignore
└── README.md

Configuration Design

Each environment has its own config file
No mixing of dev / QA / staging / prod values
Prevents accidental production misconfiguration
Example:
jdbc.url=jdbc:mysql://qa-db:3306/appdb

Python Automation Logic

The Python script:
Reads ENV and JDBC_URL from environment variables
Validates inputs
Updates only the jdbc.url key
Fails fast if validation fails
Run manually:
ENV=qa JDBC_URL=jdbc:mysql://qa-db:3306/appdb python scripts/update_jdbc.py

Ansible Deployment

The Ansible playbook:
Reads the updated config from Jenkins workspace
Copies it to the target location (simulated)
Simulates application restart
Run manually:
ENV=qa ansible-playbook -i inventory playbook.yml

Jenkins CI/CD Pipeline

The Jenkins pipeline:
Checks out code from GitHub
Sets up Python virtual environment
Installs dependencies
Runs Python script to update JDBC config
Deploys updated config using Ansible

Workspace used by Jenkins:

/var/lib/jenkins/workspace/Automation_demo_cofig_update


All updates happen inside the Jenkins workspace.
Developer local files are never modified.

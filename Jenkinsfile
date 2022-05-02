// Example Jenkins pipeline with Python
// Jenkins Setup:
// Before start jenkins, create some volume to store configurations and data for jenkins

// docker volume create jenkins-data

// docker run \
//   -u root \
//   -d \
//   --name blue-ocean \
//   -p 8080:8080 \
//   -v jenkins-data:/var/jenkins_home \
//   -v /var/run/docker.sock:/var/run/docker.sock \
//   jenkinsci/blueocean:latest

// If it meets docker permission issue with jenkins user,
// it can be modified by adding jenkins to docker group.

// ** You can setup a node to run the test. Running test on master will encounter into docker in docker issue. **

pipeline {
  agent any

  environment {
    // it can load the record key variable from credentials store
    // see https://jenkins.io/doc/book/using/using-credentials/
    // https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#handling-credentials
    SAUCE_USERNAME = credentials('sauce-username')
    SAUCE_ACCESS_KEY = credentials('sauce-access-key')
  }

  stages {
    stage('Setup Python') {
      steps {
        echo 'Setup virtualenv'
        sh 'python3 -m venv venv3'
        sh '. venv3/bin/activate'
      }
    }
    stage('Install pipenv & dependencies') {
      steps {
        echo 'Run Sauce Cypress Pipeline Test'
        sh 'pip3 install pipenv'
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('Run tests') {
      steps {
        // This step trigger the test
        echo 'Run pytest'
        sh 'pipenv run jeff-demo-desktop-eu'
      }
    }
  }
}
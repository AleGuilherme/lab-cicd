#!/bin/sh
pipeline {
    agent any
    stages {
        stage('BlueGreenFileContent') {
            steps {
                  script {
                         try {
                              env.FILENAME = readFile 'BlueGreenControl'
                              echo "${env.FILENAME}"
                         }
                         catch(Exception err_file) {
                             echo "File BlueGreenControl Not Found"
                         }
                  }
            }
        }

        stage('Build') {
            steps {
                   script {
                          sh('docker rm -f hello-${env.FILENAME}')
                          sh('docker run --name hello-${env.FILENAME} -v /root/app/${env.FILENAME}/hello.py:/usr/local/src/hello.py --net=example -d python:3 python /usr/local/src/hello.py')
                          sh('rm -f /nginx/hello.conf')
                          sh('cp /var/jenkins_home/workspace/lab-cicd_master/nginx/hello.conf /nginx/hello.conf')
                          sh('docker kill -s HUP nginx')
                         }
                  }
            }
          }
      }

pipeline {
    agent {
        label 'docker'
    }
    
    environment { 
         app_type = sh (returnStdout: true, script: 'cat BlueGreenControl')
    }

    stages {
        stage('Build') {
            steps {
                          echo ${app_type}
                          sh("docker rm -f hello-${app_type}")
                          sh("docker run --name hello-${app_type} -v /root/app/${app_type}/hello.py:/usr/local/src/hello.py --net=example -d python:3 python /usr/local/src/hello.py")
                          sh("rm -f /nginx/hello.conf")
                          sh("cp /var/jenkins_home/workspace/lab-cicd_master/nginx/hello.conf /nginx/hello.conf")
                          sh("docker kill -s HUP nginx")
                  }
            }
          }
 }

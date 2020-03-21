pipeline {
    agent any
    
    environment { 
         app_type = sh (returnStdout: true, script: 'cat BlueGreenControl').trim()
    }

    stages {
        stage('Build') {
            steps {
                echo "${app_type}"
                sh 'docker rm -f hello-${app_type} || true'
                sh 'rm -f /app/${app_type}/hello.py'
                sh 'cp /var/jenkins_home/workspace/lab-cicd_master/app/${app_type}/hello.py /app/${app_type}/hello.py'
                sh 'docker run --name hello-${app_type} -v /root/app/${app_type}/hello.py:/usr/local/src/hello.py --net=example -d python:3 python /usr/local/src/hello.py'
                sh 'rm -f /nginx/hello.conf'
                sh 'cp /var/jenkins_home/workspace/lab-cicd_master/nginx/hello.conf /nginx/hello.conf'
                sh 'docker kill -s HUP nginx'
            }
        }

       stage('Test') {
            steps {
                  sh 'cp /var/jenkins_home/workspace/lab-cicd_master/app/teste/test.py /app/teste/test.py'
                  sh 'cp /var/jenkins_home/workspace/lab-cicd_master/app/teste/app.py /app/teste/app.py'
                  sh 'docker run --rm -w/usr/local/src/ -v /root/app/teste/:/usr/local/src/ --net=example python_app python /usr/local/src/test.py'
            }
            post {
                 always {
                        junit 'test-reports/*.xml'
                 }
            }    
       }
    }
 }

pipeline {
    agent any
    
    environment { 
         app_type = sh (returnStdout: true, script: 'cat BlueGreenControl').trim()
    }

    stages {
        stage('Build') {
            steps {
                echo "${app_type}"
                sh 'docker rm -f B3Z-${app_type} || true'
                sh 'rm -f /app/${app_type}/b3z.py || true'
                sh 'cp /var/jenkins_home/workspace/lab-cicd_master/app/${app_type}/b3z.py /app/${app_type}/b3z.py'
                sh 'docker run --name B3Z-${app_type} -v /root/app/${app_type}:/app_b3z -w /app_b3z--net=example -d python:3 python b3z.py'
                sh 'rm -f /nginx/nginx_b3z.conf || true'
                sh 'cp /var/jenkins_home/workspace/lab-cicd_master/nginx/nginx_b3z.conf /nginx/nginx_b3z.conf'
                sh 'docker kill -s HUP nginx'
            }
        }

       stage('Test') {
            steps {
                   sh 'docker run --rm -v /root/app/teste:/app_python -w /app_python python_app python test.py'
            }
            post {
                 always {
                        junit 'test-reports/*.xml'
                 }
            }    
       }
    }
 }

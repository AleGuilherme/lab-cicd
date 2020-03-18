pipeline {
    agent any

    stages {
        stage('BlueGreenFileContent') {
            steps {
                  script {
                         try {
                            // String app_type = "${sh(script: 'cat BlueGreenControl', returnStdout: true)}"
                            def app_type = "green"
                             echo "${app_type}"
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
                          if (app_type.equals(green)) {
                             sh  '[[ (docker ps -f name=hello-GREEN -q) ]] && [[ (docker stop hello-GREEN && docker rm hello-GREEN) ]]'
                             sh  'docker run --name hello-GREEN -v /root/app/blue/hello.py:/usr/local/src/hello.py --net=example -d python:3 python /usr/local/src/hello.py'  
                          } else {
                              echo "green Not equal - ${app_type}"
                            }
                   }
            }
         }
                         

        stage('RedirectBlueGreen') {
            steps {
                  script {
                         try {
                             sh 'rm -f /nginx/hello.conf && cp /var/jenkins_home/workspace/lab-cicd_master/nginx/hello.conf /nginx/hello.conf'
                             sh 'docker kill -s HUP nginx'
                         }
                         catch(Exception err_file) {
                             echo "Erro no_BlueGreen!"
                         }
                  }
            }
        }
    }
}

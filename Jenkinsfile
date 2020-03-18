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
                          if (env.FILENAME == "green") {
                             sh  '[[ (docker ps -f name=hello-GREEN -q) ]] && [[ (docker stop hello-GREEN && docker rm hello-GREEN) ]]'
                             sh  'docker run --name hello-GREEN -v /root/app/blue/hello.py:/usr/local/src/hello.py --net=example -d python:3 python /usr/local/src/hello.py'  
                          } else {
                              echo "Not equal"
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

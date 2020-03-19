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

        stage('RedirectBlueGreen') {
            steps {
                  script {
                         try {
                             sh  "[[ docker ps -f name=hello-${env.FILENAME} -q ]] && [[ docker stop hello-${env.FILENAME} && docker rm hello-${env.FILENAME} ]]"
                             //sh  "docker run --name hello-${env.FILENAME} -v /root/app/blue/hello.py:/usr/local/src/hello.py --net=example -d python:3 python /usr/local/src/hello.py"  

                             sh "rm -f /nginx/hello.conf && cp /var/jenkins_home/workspace/lab-cicd_master/nginx/hello.conf /nginx/hello.conf"
                             sh "docker kill -s HUP nginx"
                         }
                         catch(Exception err_file) {
                             echo "Erro no_BlueGreen!"
                         }
                  }
            }
        }
    }
}

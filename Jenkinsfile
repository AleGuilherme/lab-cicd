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
                             echo "sh rm -f /nginx/hello.conf && cp /var/jenkins_home/workspace/lab-cicd_master/nginx/hello.conf /nginx/hello.conf"
                             echo "sh docker kill -s HUP nginx ${env.FILENAME}"
                         }
                         catch(Exception err_file) {
                             echo "Erro no_BlueGreen!"
                         }
                  }
            }
        }
    }
}

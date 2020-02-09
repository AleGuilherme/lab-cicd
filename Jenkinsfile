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
                             sh 'rm -f /root/nginx-conf.d/hello.conf && cp hello.conf /root/nginx-conf.d/hello.conf'
                             docker kill -s HUP nginx 
                         }
                         catch(Exception err_file) {
                             echo "Permission Denied!"
                         }
                  }
            }
        }
    }
}

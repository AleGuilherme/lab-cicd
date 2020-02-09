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
                             sh 'whoami'
                             sh 'cp hello.conf /root/nginx-conf.d/hello.conf'
                             sh 'docker kill -s HUP nginx'
                         }
                         catch(Exception err_file) {
                             echo "Permission denied!"
                         }
                  }
            }
        }
    }
}

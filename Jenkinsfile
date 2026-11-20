pipeline {
    agent any

    tools {
        // Debe coincidir con el nombre que pusiste en Global Tool Configuration
        'dependency-check' 'Dependency-Check'
    }

    stages {
        stage('Build') {
            steps {
                sh 'echo "Preparando proyecto..."'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Ejecutando pruebas..."'
            }
        }

        stage('Analyze') {
            steps {
                sh 'echo "Analizando codigo..."'
            }
        }

        stage('Security Test') {
    	    steps {
        	 sh '''
                   which dependency-check.sh || true
                   dependency-check.sh --project "DevSecOps-Proyecto" --scan "." --format "HTML" --out "dependency-check-report"
                  '''
                dependencyCheckPublisher pattern: 'dependency-check-report/dependency-check-report.xml'
          }
      }

        stage('Deploy') {
            steps {
                sh 'echo "Desplegando..."'
            }
        }
    }
}
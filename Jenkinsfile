pipeline {
    agent any

    tools {
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
	        withCredentials([string(credentialsId: 'nvd-api-key', variable: 'NVD_API_KEY')]) {
	            sh '''
	                mkdir -p dependency-check-report
  	              dependency-check.sh \
  	                  --project "DevSecOps-Proyecto" \
	                    --scan "." \
  	                  --format "ALL" \
        	            --out "dependency-check-report" \
                	    --nvdApiKey "$NVD_API_KEY"
            		'''
        		}
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
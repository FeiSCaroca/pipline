pipeline {
    agent any

    tools {
        'dependency-check' 'Dependency-Check'
        'hudson.plugins.sonar.SonarRunnerInstallation' 'SonarScanner'
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
                withSonarQubeEnv('SonarQube') {
                    withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                        sh '''
                            SCANNER_BIN=$(find /var/jenkins_home/tools/hudson.plugins.sonar.SonarRunnerInstallation/SonarScanner -name "sonar-scanner" -type f | head -n 1)
                            "$SCANNER_BIN" -Dsonar.token="$SONAR_TOKEN"
                        '''
                    }
                }
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

                sh '''
		  mkdir -p zap-report
		  chmod -R 777 zap-report
 		 docker run --rm --user 0:0 \
 		     -v "$(pwd)/zap-report:/zap/wrk:rw" \
   		   ghcr.io/zaproxy/zaproxy:stable \
    		  zap-baseline.py -t http://host.docker.internal:5000/hello?name=test -r zap_report.html || true
    		mod -R 777 zap-report
'''

        stage('Deploy') {
            steps {
                sh 'echo "Desplegando..."'
            }
        }
    }
}
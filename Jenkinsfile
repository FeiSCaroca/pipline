pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Preparando entorno y dependencias para la aplicación Flask...'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias o básicas...'
            }
        }
        
        stage('Analyze') {
            steps {
                echo 'Ejecutando análisis de calidad y seguridad estática con SonarQube...'
            }
        }
        
        stage('Security Test') {
            steps {
                echo 'Ejecutando OWASP Dependency-Check y OWASP ZAP...'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación en entorno de prueba...'
            }
        }
    }
}
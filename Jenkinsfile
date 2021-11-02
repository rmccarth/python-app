node {
	stage('Checkout Sourcecode') {
		checkout scm
	}
	
	stage('Perform Unit Tests') {
		sh 'mkdir results/ && python3 -m unittest tests.py'
	}
	stage('Conduct SAST') {
		sh 'bandit app/main.py -f json | tee results/sast-results-bandit.json'
	}
	stage('Archive Results') {
		archiveArtifacts artifacts: 'results/**'
	}
}


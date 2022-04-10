.PHONY: clean
clean:
	find . -name '*.pyo' -delete
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*~' -delete
	find . -name '.coverage.*' -delete

.PHONY: lint
lint:
	isort --check-only facilyst
	black facilyst -t py39 --check

.PHONY: lint-fix
lint-fix:
	isort facilyst
	black -t py39 facilyst

.PHONY: installdeps
installdeps:
	pip install --upgrade pip -q
	pip install -e .

.PHONY: installdeps-test
installdeps-test:
	pip install -e . -q
	pip install -r test-requirements.txt

.PHONY: installdeps-dev
installdeps-dev:
	pip install -e . -q
	pip install -r dev-requirements.txt

.PHONY: test
test:
	pytest facilyst/tests -n 2 --durations 20 --timeout 300 --cov=facilyst --junitxml=test-reports/git-all-tests-junit.xml

.PHONY: test-datasets
test:
	pytest facilyst/tests/dataset_tests -n 2 --durations 20 --timeout 300 --cov=facilyst --junitxml=test-reports/git-all-tests-junit.xml

.PHONY: test-models
test:
	pytest facilyst/tests/models_tests -n 2 --durations 20 --timeout 300 --cov=facilyst --junitxml=test-reports/git-all-tests-junit.xml

.PHONY: test-mocks
test:
	pytest facilyst/tests//mock_tests -n 2 --durations 20 --timeout 300 --cov=facilyst --junitxml=test-reports/git-all-tests-junit.xml

.PHONY: test-graphs
test:
	pytest facilyst/tests//graphs_tests -n 2 --durations 20 --timeout 300 --cov=facilyst --junitxml=test-reports/git-all-tests-junit.xml

.PHONY: test-utils
test:
	pytest facilyst/tests//utils_tests -n 2 --durations 20 --timeout 300 --cov=facilyst --junitxml=test-reports/git-all-tests-junit.xml
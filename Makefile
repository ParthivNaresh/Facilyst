.PHONY: lint
lint:
	isort --check-only facilyst
	black facilyst -t py39 --check
	pydocstyle facilyst/ --convention=google --add-ignore=D107 --add-select=D400 --match-dir='^(?!(tests)).*'
	flake8 facilyst

.PHONY: lint-fix
lint-fix:
	black -t py39 facilyst
	isort facilyst

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

.PHONY: tests
tests:
	pytest facilyst/tests/ -n 2 --durations 20 --timeout 300 --cov=facilyst --junitxml=test-reports/git-all-tests-junit.xml

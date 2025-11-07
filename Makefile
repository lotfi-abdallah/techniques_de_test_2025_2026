
help: ## Show this help message
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

test:
	pytest -v tests/
unit_test: 
	pytest -v tests/test_unit.py
perf_test:
	pytest -v tests/test_perf.py
coverage:
	pytest --cov=app tests/
lint:	
	flake8 --max-line-length=120 .
doc:
	pdoc -o docs/ .
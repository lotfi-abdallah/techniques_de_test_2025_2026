
.PHONY: test unit_test api_test perf_test coverage lint doc
test:
	pytest -m "not perf"
unit_test: 
	pytest -m unit
api_test:
	pytest -m api
perf_test:
	pytest -m perf
coverage:
	coverage run -m pytest
coverage-report:
	coverage report -m
coverage-html:
	coverage html
lint:	
	ruff check
doc:
	pdoc -o docs/ .
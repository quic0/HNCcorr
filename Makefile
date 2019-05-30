all: test

lint: pylint pydoc pycode

pylint:
	pylint --rcfile=.pylintrc src/hnccorr

pydoc:
	pydocstyle src/

pycode:
	pycodestyle src/ tests/

test:
	pytest

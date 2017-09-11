clean-pyc:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +
	find . -name '*~' -exec rm -rf  {} +

init:
	pip install pipenv
	pipenv install --dev

test: clean-pyc
	pipenv run python -m unittest discover

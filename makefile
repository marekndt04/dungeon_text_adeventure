black:
	black .

isort:
	isort .

mypy:
	mypy .

format: black isort

check:
	black --check .
	isort --check .
	mypy .

unittest:
	python -m unittest discover -s tests -b

test: unittest check

black:
	black .

isort:
	isort .

format: black isort

test:
	python -m unittest discover -s tests
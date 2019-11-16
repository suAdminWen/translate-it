.PHONY: test, install, publish, clean

install:
	@pip install -U pip
	@pip install -e .

test:install
	@pip install pytest
	@pytest

publish:
	@pip install 'twine>=1.5.0' wheel
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
	@make clean

clean:
	@find . -name 'dist' -print -exec rm -rf {} +
	@find . -name 'build' -print -exec rm -rf {} +
	@find . -name '.eggs' -print -exec rm -rf {} +
	@find . -name '.pytest_cache' -print -exec rm -rf {} +
	@find . -name '*.egg-info' -print -exec rm -rf {} +
	@find . -name '*.pyc' -print -exec rm -f {} +
	@find . -name '__pycache__' -print -exec rm -rf {} +
	@echo 'Done [clean]'

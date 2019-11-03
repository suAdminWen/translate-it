
publish:
	pip install 'twine>=1.5.0' wheel
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg translate_it.egg-info

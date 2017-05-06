init:
				pip install -r requirements.txt --upgrade

install:
				pip install -e .

run:
				wpt --config config.json

clean:
				find . -name "*.pyc" -exec rm -rf {} \;

package:
				rm -rf dist/
				python setup.py sdist
				python setup.py bdist_wheel

publish:
				python setup.py register
				twine upload dist/*

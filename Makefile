init:
				pip install -r requirements.txt
				pip install -e .

clean:
				find . -name "*.pyc" -exec rm -rf {} \;

package:
				python setup.py sdist
				python setup.py bdist_wheel

publish:
				python setup.py register
				twine upload dist/*

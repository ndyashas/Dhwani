help:
	@echo "Select an operation to perform from the given list";
	@echo "[ build, publish, test-publish, install, test-install, clean ]";
	@echo "Run 'make help' to show this menu again\n";

test-publish: build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish: build
	twine upload dist/*

build:
	python3 setup.py sdist bdist_wheel

test-install:
	pip install --index-url https://test.pypi.org/simple/ dhwani

install:
	python3 setup.py install

clean:
	$(RM) -r build dist *.egg-info

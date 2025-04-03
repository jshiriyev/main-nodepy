from setuptools import setup, find_packages

setup(
	name = 'nodepy',
	version = '0.0.21',
	packages = find_packages(),
	install_requires = [
		'numpy>=1.26.4',
		'scipy>=1.13.0',
		],
	)

# Run the followings from the command line to test it locally:

# python setup.py sdist bdist_wheel

# pip install dist/nodepy-{version}-py3-none-any.whl

# Run the followings from the command line to upload to pypi:

# twine upload dist/*
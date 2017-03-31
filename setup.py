from setuptools import setup

setup(
	name='flask-tutorial',
	package=['flaskr'],
	include_package_data=True,
	install_requires=[
		'flask',
	],
	setup_requires=[
		'pytest-runner',
	],
	tests_required=[
		'pytest',
	],
)
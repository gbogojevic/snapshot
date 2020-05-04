from setuptools import setup

setup(
	name='snapshoter',
	version='0.1',
	author="Me",
	author_email="me@me.com",
	description="Snapshoter is atool to manage AWS EC2 snapshots",
	license="GPLv3+",
	packages=['shotty'],
	url="https://github.com/gbogojevic/snapshot",
	install_requires=[
		'click',
		'boto3'
		],
	entry_points='''
		[console_scripts]
		shotty=shotty.shotty:cli
	''',
)
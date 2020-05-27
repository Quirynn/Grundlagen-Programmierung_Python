from setuptools import setup

requires = [
	'asyncio',
    'aiofiles',
	'starlette',
	'uvicorn',
	'pymysql',
	'sqlalchemy',
    'chameleon'
]

setup(
	name='cookbook',
	version='1.0.0',
	install_requires=requires,
	entry_points=
		"""\
		[paste.app_factory]
		main = cookbook:main
		[console_scripts]
		dbinit = cookbook.scripts.dbinit:main
		cookbook = cookbook.scripts.serve:main
		"""
)

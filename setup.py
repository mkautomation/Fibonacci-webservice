try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
    'name': 'Fibonacci webservice',
    'description': 'Fibonacci webservice',
    'author': 'Mahendra Kaushal',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mkkaushal@hotmail.com',
    'version': '1.0',
    'install_requires': ['flask'],
    'py_modules': ['fibonacci', 'endpoints', 'tests'],
    'packages': ['fibonacci', 'endpoints',  'tests'],
    'scripts': []
}

setup(**config)
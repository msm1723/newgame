try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Mint learning Python',
    'author': 'Mint the One',
    'url': 'URL your mom',
    'download_url': 'Where to download it?',
    'author_email': 'heremyname@gmail.com',
    'version': '0.0.1a1',
    'install_requires': ['pytest'],
    'packages': ['NEWGAME'],
    'scripts': ['bin/newgame'],
    'name': 'The Newgame'
}

setup(**config)

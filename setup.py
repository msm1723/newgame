try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Mint project1',
    'author': 'Mint',
    'url': 'no URL',
    'download_url': 'Where to download it.',
    'author_email': 'heremyname@gmail.com',
    'version': '0.2',
    'install_requires': ['nose'],
    'packages': ['NEWGAME'],
    'scripts': ['bin/newgame.py'],
    'name': 'newgame'
}

setup(**config)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python wrapper for Bing Search API',
    'author': 'Marshall Shen',
    'url': 'github.com/marshallshen',
    'download_url': 'Where to download it.',
    'author_email': 'shen.marshall@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['bing'],
    'scripts': [],
    'name': 'bing-python'
}

setup(**config)
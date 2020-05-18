from setuptools import setup

setup(
    name='pydownloader',
    version='1.0',
    description='Download YT videos using this simple tool!',
    author='Calamity34',
    author_email='nick.goloushckin@ya.ru',
    packages=['pydownloader'],
    install_requires=['bs4','beautifulsoup4','pytube3','requests'],
    scripts = [
        'scripts/pydownloader'
    ]
)
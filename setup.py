from setuptools import setup

setup(
    name='pythondl',
    version='1.1',
    description='Download YT videos using this simple tool!',
    author='Calamity34',
    author_email='nick.goloushckin@ya.ru',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.8"
    ],
    packages=['pythondl'],
    install_requires=['bs4','beautifulsoup4','pytube3','requests'],
    scripts = [
        'scripts/pydownloader'
    ]
)

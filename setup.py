from setuptools import find_packages, setup

setup(
    name='cl-chess',
    packages=['src'],
    version='1.2.7',
    description='A program to play chess on the command line',
    author='Marcus Buffett',
    author_email='marcusbuffett@me.com',
    url='https://github.com/marcusbuffett/command-line-chess',
    #download_url='https://github.com/peterldowns/mypackage/tarball/0.1',
    entry_points={
        'console_scripts': [
            'chess = src.main:main',
        ],
    },
    install_requires=[
        'termcolor',
        ],
    keywords=['chess', 'game'],
    classifiers=["Programming Language :: Python :: 3"],
)

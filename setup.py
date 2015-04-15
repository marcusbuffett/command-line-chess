from setuptools import setup, find_packages
setup(
    name='cl-chess',
    package_dir = {'': 'src'},
    packages=[''],
    version='1.0',
    description='A program to play chess on the command line',
    author='Marcus Buffett',
    author_email='marcusbuffett@me.com',
    url='https://github.com/marcusbuffett/command-line-chess',
    #download_url='https://github.com/peterldowns/mypackage/tarball/0.1',
    entry_points={
        'console_scripts': [
            'chess = main:main',
        ],
    },
    keywords=['chess', 'game'],
    classifiers=["Programming Language :: Python :: 3"],
)

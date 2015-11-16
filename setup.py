#!/usr/bin/env python2

from distutils.core import setup
import codecs
import os.path as path

cwd = path.dirname(__file__)
version = '0.0.0'
with codecs.open(path.join(cwd, 'mlbgame/version.py'), 'r', 'ascii') as f:
    exec(f.read())
    version = __version__
assert version != '0.0.0'

setup(
    name='mlbgame',
    author='Zach Panzarino',
    author_email='zachary@panzarino.com',
    version=version,
    license='MIT',
    description='An API to retrieve and read MLB GameDay JSON and XML data',
    long_description='An API to retrieve and read MLB GameDay JSON and XML data',
    url='https://github.com/zachpanz88/mlbgame',
    classifiers=[
        'License :: MIT License',
        'Development Status :: Initial Development',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    platforms='ANY',
    packages=['mlbgame'],
    package_data={'mlbgame': ['gameday-data/*.xml.gz']},
    scripts=['scripts/mlbgame-update-games'],
)
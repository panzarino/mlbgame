#!/usr/bin/env python

from distutils.core import setup
import codecs
import os.path as path

# where this file is located
cwd = path.dirname(__file__)

# get full description from rst file
longdesc = codecs.open(path.join(cwd, 'description.rst'), 'r', 'ascii').read()

version = '0.0.0'
# read version file to get version
with codecs.open(path.join(cwd, 'mlbgame/version.py'), 'r', 'ascii') as f:
    exec(f.read())
    version = __version__
# make sure version is not default
# make sure file reading worked
assert version != '0.0.0'

# download link based off tagged releases
download_link = 'https://github.com/zachpanz88/mlbgame/archive/v%s.zip' % (version)

# setup options
setup(
    name='mlbgame',
    author='Zach Panzarino',
    author_email='zach@panz.io',
    version=version,
    license='MIT',
    description='An API to retrieve and read MLB GameDay XML data',
    long_description=longdesc,
    url='https://github.com/zachpanz88/mlbgame',
    download_url=download_link,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Topic :: Other/Nonlisted Topic',
    ],
    keywords=[
        'MLB',
        'baseball',
        'Major League Baseball',
        'baseball scores',
        'baseball stats',
        'baseball data',
        'MLB GameDay',
    ],
    platforms='ANY',
    packages=['mlbgame'],
    package_data={'mlbgame': ['gameday-data/*/*/*/*.xml.gz', 'gameday-data/default.xml']},
    data_files=[('docs', ['README.md', 'LICENSE', 'description.rst'])],
    scripts=['scripts/mlbgame-update'],
    install_requires=['lxml'],
)

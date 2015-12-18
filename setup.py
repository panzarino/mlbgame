#!/usr/bin/env python2

from distutils.core import setup
import codecs
import os.path as path

cwd = path.dirname(__file__)

longdesc = codecs.open(path.join(cwd, 'longdesc.rst'), 'r', 'ascii').read()

version = '0.0.0'
with codecs.open(path.join(cwd, 'mlbgame/version.py'), 'r', 'ascii') as f:
    exec(f.read())
    version = __version__
assert version != '0.0.0'

download_link = 'https://github.com/zachpanz88/mlbgame/archive/v%s.zip' % (version)

setup(
    name='mlbgame',
    author='Zach Panzarino',
    author_email='zachary@panzarino.com',
    version=version,
    license='MIT',
    description='An API to retrieve and read MLB GameDay XML data',
    long_description=longdesc,
    url='https://github.com/zachpanz88/mlbgame',
    download_url=download_link,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Natural Language :: English',
        'Topic :: Other/Nonlisted Topic',
    ],
    keywords=[
        'MLB',
        'baseball',
        'Major League Baseball',
        'baseball scores',
        'baseball data',
        'MLB GameDay',
    ],
    platforms='ANY',
    packages=['mlbgame'],
    package_data={'mlbgame': ['gameday-data/*/*/*/*.xml.gz']},
    data_files=[('docs', ['README.md', 'LICENSE', 'longdesc.rst'])],
    scripts=['scripts/mlbgame-update-games'],
)
# -*- coding: utf-8 -*-

import io
from setuptools import setup
import sys

requires = ['Django >= 1.4', 'six>=1.4.1']
tests_require = requires


def _read_file_py2_compat(filename):
    # Return str (bytestring) on Python 2, str (unicode string) on Python 3.
    # Assumes the file is encoded with utf-8.
    if sys.version_info < (3,):
        return open(filename).read()
    return io.open(filename, encoding='utf-8').read()


setup(
    name="dj-inmemorystorage",
    description="A non-persistent in-memory data storage backend for Django.",
    version="1.4.0",
    url="https://github.com/waveaccounting/dj-inmemorystorage",
    license=_read_file_py2_compat('LICENSE'),
    long_description=_read_file_py2_compat('README.rst'),
    author='Cody Soyland, Seán Hayes, Tore Birkeland, Nick Presta',
    author_email='opensource@waveapps.com',
    packages=[
        'inmemorystorage',
    ],
    zip_safe=True,
    install_requires=requires,
    tests_require=tests_require,
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

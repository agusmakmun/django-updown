#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('updown')


setup(
    name='django-updown-ratings',
    version=version,
    description='Reusable Django application for youtube like up and down voting.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Daniel Banck, Agus Makmun',
    author_email='dbanck@weluse.de',
    url='http://github.com/agusmakmun/django-updown-ratings/tree/master',
    packages=find_packages(exclude=["*demo"]),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

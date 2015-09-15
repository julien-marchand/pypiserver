#! /usr/bin/env python

import sys, os

try:
    from setuptools import setup
    extra = {'entry_points': {
                'paste.app_factory': ['main=pypiserver:paste_app_factory'],
                'console_scripts': ['pypi-server=pypiserver.__main__:main']
            }}
except ImportError:
    from distutils.core import setup
    extra = dict(scripts=["pypi-server"])

if sys.version_info >= (3, 0):
    exec("def do_exec(co, loc): exec(co, loc)\n")
    tests_require = []
else:
    exec("def do_exec(co, loc): exec co in loc\n")
    tests_require =  ['mock']


def get_version():
    d = {}
    try:
        do_exec(open("pypiserver/__init__.py").read(), d)
    except (ImportError, RuntimeError):
        pass
    return d["__version__"]


setup(name="pypiserver",
      description="A minimal PyPI server for use with pip/easy_install.",
      long_description=open("README.rst").read(),
      version=get_version(),
      packages=["pypiserver"],
      package_data={'pypiserver': ['welcome.html']},
      tests_require=tests_require,
        url="https://github.com/pypiserver/pypiserver",
      maintainer="Ralf Schmitt, Kostis Anagnostopoulos",
      maintainer_email="ralf@systemexit.de, ankostis@gmail.com",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "License :: OSI Approved :: zlib/libpng License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Software Distribution"],
      zip_safe=False,
      **extra)

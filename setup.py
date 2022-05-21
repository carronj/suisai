#!/usr/bin/env python
import sys
from setuptools import setup # to support "develop" mode
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.verbose = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

extras_require={'plots':  ["colorspacious", "viscm"]}

setup(
      name    = "suisai",
      version = "1.0",
      author  = "Yuuki Omori",
      url     = 'https://github.com/yomori/suisai',
      author_email = "yomori@uchicago.edu",
      download_url = 'https://github.com/matplotlib/cmocean/tarball/2.0',
      description  = ("Colormaps"),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      classifiers=[
                   "Development Status :: 3 - Alpha",
                  ],
      package_data = {'suisai': ['rgb/*.txt'],},

      packages    = ["suisai"],
      ext_package = 'suisai',
      scripts     = [],
      keywords    = ['colormaps', 'visualization'],
      setup_requires   = ['setuptools'],
      install_requires = ['matplotlib', 'numpy'],
      tests_require=['pytest'],
      extras_require=extras_require
    )

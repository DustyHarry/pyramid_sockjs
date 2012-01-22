import os
import sys
import logging
import multiprocessing # atexit exception
from setuptools import setup, find_packages

version='0.1dev'

install_requires = ['setuptools',
                    'pyramid >= 1.3a6',
                    'gevent >= 1.0dev',
                    'gevent-websocket >= 0.3.0-dev',
                    ]

tests_require = install_requires + ['nose']

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(name='pyramid_sockjs',
      version=version,
      description=('SockJS server implementation.'),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: Implementation :: CPython",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          'Topic :: Internet :: WWW/HTTP :: WSGI'],
      author='Nikolay Kim',
      author_email='fafhrd91@gmail.com',
      url='https://github.com/fafhrd91/pyramid_sockjs/',
      license='BSD',
      packages=find_packages(),
      install_requires = install_requires,
      tests_require = tests_require,
      test_suite = 'nose.collector',
      include_package_data = True,
      zip_safe = False,
      entry_points = {
          'paste.server_runner': [
              'server = pyramid_sockjs.paster:gevent_server_runner',
              ],
          },
      )
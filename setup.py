#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages
setup(name='LitleSdkPython',
      version='8.25.0',
      description='Litle & Co. SDK for Python',
      author='Litle & Co',
      author_email='SDKSupport@litle.com',
      url='http://www.litle.com/developers',
      packages=['litleSdkPython'],
      install_requires=[
                        'PyXB',
                        'paramiko'],
      dependency_links =[
                         'https://pypi.python.org/packages/source/P/PyXB/PyXB-1.1.5.tar.gz#md5=95ce5cd2ad7abfead042896f88d25eea',
                         'https://pypi.python.org/packages/source/p/paramiko/paramiko-1.14.0.tar.gz#md5=e26324fd398af68ad506fe98853835c3'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Environment :: MacOS X'
          'Environment :: Plugins'
          'Environment :: Win32 (MS Windows)'
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent'
          'Operating System :: MacOS',
          'Operating System :: Microsoft',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Office/Business :: Financial',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
     )
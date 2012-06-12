#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages
setup(name='LitleSdkPython',
      version='8.13.0',
      description='Litle & Co. SDK for Python',
      author='Litle & Co',
      author_email='SDKSupport@litle.com',
      url='http://www.litle.com/developers',
      packages=['litleSdkPython'],
      install_requires=[
                        'PyXB'],
      dependency_links =[
                         'http://pypi.python.org/packages/source/P/PyXB/PyXB-full-1.1.3.tar.gz#md5=62f4e37baa59d9fc9df5f7186e7d63a2'],
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
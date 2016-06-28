#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages
setup(name='LitleSdkPython',
      version='8.29.1',
      description='Vantiv eCommerce SDK for Python',
      author='Vantiv eCommerce',
      author_email='SDKSupport@vantiv.com',
      url='http://www.vantiv.com/developers',
      packages=['litleSdkPython'],
      install_requires=[
                        'PyXB==1.1.5',
                        'paramiko==1.14.0'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Environment :: MacOS X',
          'Environment :: Plugins',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
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

#! /usr/bin/env python
#! -*- coding: utf-8 *-*-

from setuptools import setup, find_packages

readme = open('README.md', 'r').read()
setup(
    name='webpagetest',
    version='0.2',
    url='https://github.com/khilnani/webpagetest.py',
    license='MIT',
    author='khilnani',
    author_email='nik@khilnani.org',
    description='Python CLI to schedule tests with WebPageTest.org.',
    include_package_data=True,
    long_description=readme,
    packages=find_packages(),
    install_requires=['requests','texttable'],
    entry_points={
        'console_scripts': [
            'wpt = webpagetest',
            ]
    },
    keywords=('webpagetest', 'wpt'),
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],  
    ) 

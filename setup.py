# -*- coding: utf-8 -*-
"""
Setup module for recipe_generator
"""

import sys
from setuptools import setup, find_packages

install_requires = ['bs4', 'termcolor']

setup(name='feedme',
      version='1.0',
      description='gib me dat food eh',
      url='https://github.com/khavernathy/recipe_generator',
      author='Douglas Franz',
      author_email='nah@nah.com',  
      install_requires=install_requires,
      zip_safe=False,  # Use of __file__ and __path__ in some code makes it unusable from zip
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ],
      platforms=['any'],
      license='MIT',
)

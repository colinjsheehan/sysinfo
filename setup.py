'''
Created on 8 Feb 2018

@author: colinsheehan
'''
from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Colin Sheehan",
      author_email = "colinjohn@outlook.ie",
      licence="GPL3",
      package_dir = {'': 'systeminfo'},
      packages=[''],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.sysinfo:main']
          }
      )
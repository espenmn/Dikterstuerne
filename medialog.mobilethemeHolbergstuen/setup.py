from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n')

setup(name='medialog.mobilethemeHolbergstuen',
      version=version,
      description="A diazo theme for holbergstuen",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Holbergstuen medialog theme',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/medialog.mobilethemeHolbergstuen',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'ftw.mobilenavigation',
          'plone.api',
          'plone.app.themingplugins',
          'z3c.jbot',
          
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )

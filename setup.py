# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os


def read(*paths):
    return open(os.path.join(os.path.dirname(__file__), *paths)).read()

version = '0.5'

setup(name='collective.prettyphoto',
      version=version,
      description="prettyPhoto integration for Plone.",
      long_description='\n\n'.join([
          read("README.rst"),
          read("docs", "HISTORY.rst"),
      ]),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone :: 3.3",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Python",
      ],
      keywords='Plone Lightbox jQuery',
      author='Thomas Massmann',
      author_email='thomas.massmann@inqbus.de',
      url='https://github.com/collective/collective.prettyphoto',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing[robot]>=4.2.2',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

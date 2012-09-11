from setuptools import setup, find_packages
import os

version = '0.4.5.1'

setup(name='collective.prettyphoto',
      version=version,
      description="prettyPhoto integration for Plone.",
      long_description=open("README.rst").read() + "\n\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
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
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

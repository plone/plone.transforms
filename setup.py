from setuptools import setup, find_packages

version = '1.1a1'

setup(name='plone.transforms',
      version=version,
      description="Transformation registry and utilities.",
      long_description=(
              open('README.txt').read() + '\n' +
              open('CHANGES.txt').read()
      ),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='Plone Transformation',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.transforms',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.configuration',
          'zope.dottedname',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.security',
          'zope.testing',
          'ZODB3',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

from setuptools import setup, find_packages

version = '1.0a3'

setup(name='plone.transforms',
      version=version,
      description="Transformation registry and utilities.",
      long_description="""\
""",
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
          'zope.interface',
          'zope.component',
          'zope.dottedname',
      ],
      )

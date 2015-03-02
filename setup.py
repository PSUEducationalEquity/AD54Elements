from setuptools import setup, find_packages

version="4.2"

setup(name='Products.AD54Elements',
      version=version,
      description="A product to add Penn State policy-mandated elements to a Plone site",
      long_description=open("README.txt").read() + "\n" +
                       open("HISTORY.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='WebLion Group, Penn State University',
      author_email='support@weblion.psu.edu',
      url='http://weblion.psu.edu/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone>=4.0b1',
          'plone.browserlayer',
          # -*- Extra requirements: -*-
      ],
      extras_require=dict(test=['plone.app.testing','BeautifulSoup']),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )


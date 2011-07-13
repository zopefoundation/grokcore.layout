from setuptools import setup, find_packages
import os

readme_filename = os.path.join('src', 'grokcore', 'layout', 'README.txt')
long_description = open(readme_filename).read() + '\n\n' + \
                   open('CHANGES.txt').read()

test_requires = [
    'zope.annotation',
    'zope.container',
    'zope.schema',
    'zope.security',
    'zope.session',
    'zope.site',
    'zope.testing',
    'zope.traversing',
    ]

setup(name='grokcore.layout',
      version='1.5dev',
      description="A layout component package for zope3 and Grok.",
      long_description = long_description,
      classifiers=[
          "Framework :: Zope3",
          "Programming Language :: Python",
          "Programming Language :: Zope",
          "Intended Audience :: Developers",
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='grok layout zope3 pagelet theming',
      author='Souheil Chelfouh',
      author_email='trollfot@gmail.com',
      url='http://pypi.python.org/pypi/grokcore.layout',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['grokcore'],
      include_package_data=True,
      zip_safe=False,
      extras_require={'test': test_requires},
      install_requires=[
          'grokcore.component',
          'grokcore.formlib',
          'grokcore.security',
          'grokcore.view >= 2.3',
          'martian',
          'setuptools',
          'zope.authentication',
          'zope.component >= 3.9.1',
          'zope.errorview',
          'zope.interface',
          'zope.publisher',
          ],
      )

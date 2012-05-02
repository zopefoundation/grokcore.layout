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
      version='1.5.2.dev0',
      description="A layout component package for zope3 and Grok.",
      long_description = long_description,
      classifiers=['Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Zope Public License',
                   'Programming Language :: Python',
                   'Framework :: Zope3',
                   ],
      keywords='grok layout zope3 pagelet theming',
      author='Grok Team',
      author_email='grok-dev@zope.org',
      url='http://grok.zope.org',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['grokcore'],
      include_package_data=True,
      zip_safe=False,
      extras_require={'test': test_requires},
      install_requires=[
          'grokcore.component >= 2.5',
          'grokcore.security >= 1.6',
          'grokcore.view >= 2.7',
          'martian >= 0.14',
          'setuptools',
          'zope.authentication',
          'zope.component >= 3.9.1',
          'zope.errorview',
          'zope.interface',
          'zope.publisher',
          ],
      )

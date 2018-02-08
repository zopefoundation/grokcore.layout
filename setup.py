import os
from setuptools import setup, find_packages


readme_filename = os.path.join('src', 'grokcore', 'layout', 'README.txt')


long_description = (
    open(readme_filename).read() +
    '\n\n' +
    open('CHANGES.txt').read())


test_requires = [
    'zope.app.wsgi[test]',
    'zope.annotation',
    'zope.container',
    'zope.schema',
    'zope.security',
    'zope.session',
    'zope.site',
    'zope.testbrowser',
    'zope.testing',
    'zope.traversing',
    ]


setup(
    name='grokcore.layout',
    version='3.0.3',
    description="A layout component package for zope3 and Grok.",
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
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
        'grokcore.view >= 3.0.3',
        'martian >= 0.14',
        'setuptools',
        'zope.authentication',
        'zope.component >= 3.9.1',
        'zope.errorview',
        'zope.interface',
        'zope.publisher',
        ],
)

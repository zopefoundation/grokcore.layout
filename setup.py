import os

from setuptools import find_packages
from setuptools import setup


readme_filename = os.path.join('src', 'grokcore', 'layout', 'README.rst')


long_description = (
    open(readme_filename).read() +
    '\n\n' +
    open('CHANGES.rst').read())


test_requires = [
    'zope.annotation',
    'zope.app.wsgi[test]',
    'zope.container',
    'zope.login',
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
    version='4.0',
    description="A layout component package for Grok.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Zope :: 3',
    ],
    keywords='grok layout zope3 pagelet theming',
    author='Grok Team',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/grokcore.layout',
    license='ZPL 2.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
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

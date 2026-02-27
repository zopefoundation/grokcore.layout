import doctest
import importlib.resources
import unittest

from zope.testing import renormalizing

import grokcore.layout.tests


layer = grokcore.layout.tests.GrokcoreLayoutLayer(grokcore.layout.tests)


def make_test(dottedname):
    checker = renormalizing.RENormalizing()
    test = doctest.DocTestSuite(
        dottedname,
        checker=checker,
        optionflags=(
            doctest.ELLIPSIS +
            doctest.NORMALIZE_WHITESPACE))
    test.layer = layer
    return test


def suiteFromPackage(name):
    parent = __name__.rsplit('.', 1)[0]
    files = importlib.resources.files(parent).joinpath(name).iterdir()
    suite = unittest.TestSuite()
    for filepath in files:
        filename = filepath.name
        if not filename.endswith('.py'):
            continue
        if filename.endswith('_fixture.py'):
            continue
        if filename == '__init__.py':
            continue
        dottedname = f'grokcore.layout.tests.{name}.{filename[:-3]}'
        suite.addTest(make_test(dottedname))
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['layout', 'models', 'errors']:
        suite.addTest(suiteFromPackage(name))
    return suite

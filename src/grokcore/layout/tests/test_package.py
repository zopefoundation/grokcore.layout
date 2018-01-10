# -*- coding: utf-8 -*-
import doctest
import grokcore.layout.tests
import pkg_resources
import unittest

from zope.testing import renormalizing


layer = grokcore.layout.tests.GrokcoreLayoutLayer(grokcore.layout.tests)


def make_test(dottedname):
    checker = renormalizing.RENormalizing()
    test = doctest.DocTestSuite(
        dottedname,
        checker=checker,
        optionflags=(
            doctest.ELLIPSIS +
            doctest.NORMALIZE_WHITESPACE +
            renormalizing.IGNORE_EXCEPTION_MODULE_IN_PYTHON2))
    test.layer = layer
    return test


def suiteFromPackage(name):
    files = pkg_resources.resource_listdir(__name__, name)
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename.endswith('_fixture.py'):
            continue
        if filename == '__init__.py':
            continue
        dottedname = 'grokcore.layout.tests.%s.%s' % (name, filename[:-3])
        suite.addTest(make_test(dottedname))
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['layout', 'models', 'errors']:
        suite.addTest(suiteFromPackage(name))
    return suite

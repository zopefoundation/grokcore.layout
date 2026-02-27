import doctest
import importlib.resources
import unittest

import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi

import grokcore.layout.tests.functional


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.layout.tests.functional, allowTearDown=True)


def suiteFromPackage(name):
    parent = __name__.rsplit('.', 1)[0]
    files = importlib.resources.files(parent).joinpath(name).iterdir()
    suite = unittest.TestSuite()
    getRootFolder = layer.getRootFolder
    globs = dict(
        getRootFolder=getRootFolder,
    )
    optionflags = (
        doctest.ELLIPSIS +
        doctest.NORMALIZE_WHITESPACE +
        doctest.REPORT_NDIFF
    )

    for filepath in files:
        filename = filepath.name
        if filename == '__init__.py':
            continue

        test = None
        if filename.endswith('.py'):
            dottedname = 'grokcore.layout.tests.{}.{}'.format(
                name, filename[:-3])
            test = doctest.DocTestSuite(
                dottedname,
                extraglobs=globs,
                optionflags=optionflags)
            test.layer = layer
            test.layer = layer
        if test is not None:
            suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in [
            'functional'
    ]:
        suite.addTest(suiteFromPackage(name))
    return suite

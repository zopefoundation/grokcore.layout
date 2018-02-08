import doctest
import grokcore.layout.tests.functional
import unittest
import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi

from pkg_resources import resource_listdir


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.layout.tests.functional, allowTearDown=True)


def suiteFromPackage(name):
    files = resource_listdir(__name__, '{}'.format(name))
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

    for filename in files:
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

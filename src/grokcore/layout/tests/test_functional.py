import doctest
import grokcore.layout.tests.functional
import re
import unittest
import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi

from pkg_resources import resource_listdir
from zope.testing import renormalizing


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.layout.tests.functional, allowTearDown=True)


checker = renormalizing.RENormalizing([
    # Accommodate to exception wrapping in newer versions of mechanize
    (re.compile(r'httperror_seek_wrapper:', re.M), 'HTTPError:'),
    ])


def suiteFromPackage(name):
    files = resource_listdir(__name__, '{}'.format(name))
    suite = unittest.TestSuite()
    getRootFolder = layer.getRootFolder
    globs = dict(
        getRootFolder=getRootFolder,
        )
    optionflags = (
        renormalizing.IGNORE_EXCEPTION_MODULE_IN_PYTHON2 +
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
                checker=checker,
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

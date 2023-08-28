import doctest
import unittest

from grokcore.component.testing import grok_component

import grokcore.layout.tests


def test_suite():
    optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    globs = {'grok_component': grok_component, '__name__': 'grokcore.layout'}
    suite = unittest.TestSuite()

    suite.addTest(
        doctest.DocFileSuite(
            '../README.rst',
            optionflags=optionflags,
            globs=globs))
    suite.layer = grokcore.layout.tests.ZCMLFileLayer(grokcore.layout.tests)

    return suite

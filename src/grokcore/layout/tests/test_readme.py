# -*- coding: utf-8 -*-

import doctest
import unittest
import grokcore.layout.tests
from grokcore.component.testing import grok_component


def test_suite():
    optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    globs = {'grok_component': grok_component, '__name__': 'grokcore.layout'}
    suite = unittest.TestSuite()

    suite.addTest(
        doctest.DocFileSuite(
            '../README.txt',
            optionflags=optionflags,
            globs=globs))
    suite.layer = grokcore.layout.tests.ZCMLFileLayer(grokcore.layout.tests)

    return suite

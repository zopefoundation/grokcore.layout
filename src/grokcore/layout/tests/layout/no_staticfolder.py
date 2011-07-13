"""
  >>> from grokcore.layout import ILayout
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> mongo = Dummy()
  >>> mylayout = getMultiAdapter((request, mongo), ILayout)
  >>> print mylayout.static
  None
"""

import grokcore.component as grok
from grokcore.layout import Layout


class Dummy(grok.Context):
    pass

class MyLayout(Layout):
    
    def render(self):
        return ""

"""
  >>> from megrok.layout import ILayout
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> from megrok.layout.tests.layout.static_fixture.simple import Dummy 
  >>> mongo = Dummy()
  >>> mylayout = getMultiAdapter((request, mongo), ILayout)
  >>> mylayout.static
  <grokcore.view.ftests.staticdir.simple.DummyResource object at 0...>
"""

import grokcore.component as grok
from megrok.layout import Layout
from grokcore.view.ftests.staticdir.simple import DummyResource

import zope.component
import zope.interface
from zope.publisher.interfaces.browser import IBrowserRequest


zope.component.provideAdapter(factory=DummyResource,
    adapts=(IBrowserRequest,),
    provides=zope.interface.Interface,
    name='megrok.layout.tests.layout.static_fixture')

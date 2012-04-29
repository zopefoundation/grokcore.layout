"""
  >>> from grokcore.layout import ILayout
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> from grokcore.layout.tests.layout.static_fixture.simple import Dummy
  >>> mongo = Dummy()
  >>> mylayout = getMultiAdapter((request, mongo), ILayout)
  >>> mylayout.static
  <grokcore.view.ftests.static.simple.DummyResource object at 0...>
"""

import grokcore.component as grok
from grokcore.layout import Layout
from grokcore.view.ftests.static.simple import DummyResource

import zope.component
import zope.interface
from zope.publisher.interfaces.browser import IBrowserRequest


zope.component.provideAdapter(factory=DummyResource,
    adapts=(IBrowserRequest,),
    provides=zope.interface.Interface,
    name='grokcore.layout.tests.layout.static_fixture')

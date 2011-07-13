"""
  >>> from grokcore.layout import ILayout
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> mammoth = Mammoth()
  >>> mylayout = getMultiAdapter((request, mammoth), ILayout)
  >>> ILayout.providedBy(mylayout)
  True

  >>> mylayout.context
  <grokcore.layout.tests.layout.layout.Mammoth object at ...>

  >>> mylayout.render()
  '<div> MyLayout </div>'

  >>> elephant = Elephant()
  >>> mycontextlayout = getMultiAdapter((request, elephant), ILayout)
  >>> mycontextlayout.render()
  '<div> MyContextLayout </div>'
"""

import grokcore.component as grok
from zope.interface import Interface
from grokcore.layout import Layout


class Mammoth(grok.Context):
    pass


class Elephant(grok.Context):
    pass


class MyLayout(Layout):
    grok.context(Interface)

    def render(self):
        return "<div> MyLayout </div>"


class MyContextLayout(Layout):
    grok.context(Elephant)

    def render(self):
        return "<div> MyContextLayout </div>"

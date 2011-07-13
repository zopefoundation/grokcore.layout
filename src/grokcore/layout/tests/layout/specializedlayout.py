"""
  >>> one = One()
  >>> two = Two()

  >>> from zope.publisher.browser import TestRequest
  >>> from zope.interface import directlyProvides
  >>> from zope.component import getMultiAdapter

  >>> request = TestRequest()

We test on the first layer layer::

  >>> directlyProvides(request, IALayer)
  >>> view = getMultiAdapter((one, request), name="myview")
  >>> print view()
  Layout A for context One

  >>> view = getMultiAdapter((two, request), name="myview")
  >>> print view()
  Layout A for context Two

We switch the layer::

  >>> directlyProvides(request, IBLayer)
  >>> view = getMultiAdapter((one, request), name="myview")
  >>> print view()
  Layout B for context One

  >>> view = getMultiAdapter((two, request), name="myview")
  >>> print view()
  Layout B for context Two

"""
import grokcore.view as grok
from zope.interface import Interface
from grokcore.layout import Layout, Page
from grokcore.view import IDefaultBrowserLayer


class IALayer(IDefaultBrowserLayer):
    pass


class IBLayer(IALayer):
    pass


class One(grok.Context):
    pass


class Two(One):
    pass


class AOneLayout(Layout):
    grok.context(One)
    grok.layer(IALayer)

    def render(self):
        return "Layout A for context One"


class ATwoLayout(Layout):
    grok.context(Two)
    grok.layer(IALayer)

    def render(self):
        return "Layout A for context Two"


class BOneLayout(Layout):
    grok.context(One)
    grok.layer(IBLayer)

    def render(self):
        return "Layout B for context One"


class BTwoLayout(Layout):
    grok.context(Two)
    grok.layer(IBLayer)

    def render(self):
        return "Layout B for context Two"


class MyView(Page):
    grok.context(Interface)
    grok.layer(IALayer)

    def render(self):
        return "MyView on IALayouer"

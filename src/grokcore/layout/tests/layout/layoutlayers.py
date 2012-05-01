"""
  >>> a = A()
  >>> b = B()

  >>> from zope.publisher.browser import TestRequest
  >>> from zope.interface import directlyProvides
  >>> from zope.component import getMultiAdapter

  >>> request = TestRequest()

  >>> directlyProvides(request, IDefaultLayer)
  >>> view = getMultiAdapter((a, request), name="myview")
  >>> print view()
  A Layout

  >>> directlyProvides(request, IAnotherLayer)
  >>> view = getMultiAdapter((a, request), name="myview")
  >>> print view()
  A2 Layout

  >>> view = getMultiAdapter((b, request), name="myview")
  >>> print view()
  B Layout
"""

import grokcore.view as grok
from grokcore.layout import Layout, Page
from zope.interface import Interface


class IDefaultLayer(grok.IDefaultBrowserLayer):
    pass


class IAnotherLayer(grok.IDefaultBrowserLayer):
    pass


class A(grok.Context):
    pass


class B(grok.Context):
    pass


class ALayout(Layout):
    grok.context(A)
    grok.layer(IDefaultLayer)

    def render(self):
        return "A Layout"


class A2Layout(Layout):
    grok.context(A)
    grok.layer(IAnotherLayer)

    def render(self):
        return "A2 Layout"


class BLayout(Layout):
    grok.context(B)
    grok.layer(IAnotherLayer)

    def render(self):
        return "B Layout"


class MyViewA(Page):
    grok.context(Interface)
    grok.name('myview')
    grok.layer(IDefaultLayer)

    def render(self):
        return "MYVIEW"


class MyViewB(Page):
    grok.context(Interface)
    grok.name('myview')
    grok.layer(IAnotherLayer)

    def render(self):
        return "MYVIEW"

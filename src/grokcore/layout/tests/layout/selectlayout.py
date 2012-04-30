"""
  >>> one = One()

  >>> from zope.publisher.browser import TestRequest
  >>> from zope.component import getMultiAdapter

  >>> request = TestRequest()

We test that we can retrieve the default layout for the page that
doesn't select any specific layout::

  >>> view = getMultiAdapter((one, request), name="viewone")
  >>> print view()
  Layout One

We test that we can retrieve the default layout for the page that
select a specific layout::

  >>> view = getMultiAdapter((one, request), name="viewtwo")
  >>> print view()
  Layout Two

"""
import grokcore.view as grok
from zope.interface import Interface
from grokcore.layout import Layout, Page, ILayout, layout


class One(grok.Context):
    pass


class LayoutOne(Layout):
    grok.context(One)

    def render(self):
        return "Layout One"


class ILayoutTwo(ILayout):
    pass


class LayoutTwo(Layout):
    grok.context(One)
    grok.provides(ILayoutTwo)

    def render(self):
        return "Layout Two"


class ViewOne(Page):
    grok.context(Interface)

    def render(self):
        return "MyView on regular layout"


class ViewTwo(Page):
    grok.context(Interface)
    layout(ILayoutTwo)

    def render(self):
        return "MyView on layout two"

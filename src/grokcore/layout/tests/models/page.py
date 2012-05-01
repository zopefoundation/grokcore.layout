"""
  >>> from grokcore.layout import ILayout
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> cow = Cow()
  >>> mylayout = getMultiAdapter((request, cow), ILayout)
  >>> myview = getMultiAdapter((cow, request), name='myview')

  >>> print myview()
  <html>
   <body>
     <div class="layout"><p> My nice Content </p></div>
   </body>
  </html>

  >>> myview
  <grokcore.layout.tests.models.page.MyView object at ...>
  >>> myview.layout
  <grokcore.layout.tests.models.page.Master object at ...>
  >>> print myview.content()
  <p> My nice Content </p>

"""
import grokcore.component as grok
from grokcore.view import templatedir
from grokcore.layout import Layout, Page
from zope import interface

templatedir('templates')

class Cow(grok.Context):
    pass

class Master(Layout):
    grok.name('master')
    grok.context(Cow)

class MyView(Page):
    grok.context(interface.Interface)
    grok.name('myview')

    def render(self):
        return "<p> My nice Content </p>"

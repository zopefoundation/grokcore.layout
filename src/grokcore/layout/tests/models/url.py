"""
  >>> from zope.component.hooks import getSite

  >>> site = getSite()
  >>> site
  <zope.site.folder.Folder object at ...>

  >>> helmut = site['helmut'] = Panda()

  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> view = getMultiAdapter((helmut, request), name='index')
  >>> view
  <megrok.layout.tests.models.url.Index object at ...>

  >>> print view.application_url()
  http://127.0.0.1

  >>> form = getMultiAdapter((helmut, request), name='form')
  >>> form
  <megrok.layout.tests.models.url.BearForm object at ...>

  >>> print form.application_url()
  http://127.0.0.1

"""

import grokcore.view as grok
from megrok.layout import Page, Layout, Form
from zope.interface import Interface, implements

grok.templatedir("templates")


class IBear(Interface):
    pass


class Panda(grok.Context):
    implements(IBear)


class Master(Layout):
    grok.context(IBear)


class BearForm(Form):
    grok.name('form')
    grok.context(IBear)
    

class Index(Page):
    grok.context(IBear)

    def render(self):
        return u"A view"

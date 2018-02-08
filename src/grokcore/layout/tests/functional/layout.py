"""
  >>> getRootFolder()["manfred"] = Mammoth()
  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@say_my_name")
  >>> print(browser.contents)
  <html><body>My name is Paige</body></html>

  >>> print(browser.headers)
  Status: 200 Ok
  Content-Length: 42
  Content-Type: text/html;charset=utf-8
"""


import grokcore.component as grok
from grokcore.view import require
from grokcore.layout import Layout, Page


class Mammoth(grok.Context):
    name = u'Paige'


class MammothLayout(Layout):
    grok.context(Mammoth)

    def render(self):
        return '<html><body>{}</body></html>'.format(self.view.content())


class MammothPage(Page):
    grok.name('say_my_name')
    grok.context(Mammoth)
    require('zope.Public')

    def render(self):
        return 'My name is {}'.format(self.context.name)

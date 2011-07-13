"""
  >>> from megrok.layout import ILayout
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest

  >>> kitty = Cat()
  >>> request = TestRequest()
  >>> mylayout = getMultiAdapter((request, kitty), ILayout)
  >>> myview = getMultiAdapter((kitty, request), name='utils')
  >>> myform = getMultiAdapter((kitty, request), name='formutils')

  >>> print myview.flash(u'test')
  Traceback (most recent call last):
  ...
  NoInteraction

  >>> from zope.security.management import newInteraction
  >>> newInteraction(request)

  >>> print myview.flash(u'test')
  True

  >>> print myform.flash(u'some form message')
  True

  >>> from grokcore.message import receive
  >>> messages = [i for i in receive()]
  >>> len(messages)
  2

  >>> print ", ".join([msg.message for msg in messages])
  test, some form message

  >>> from zope.security.management import endInteraction
  >>> endInteraction()

"""
import grokcore.component as grok
from grokcore.view import templatedir
from zope.interface import Interface
from megrok.layout import Layout, Page, Form

templatedir('templates')


class Cat(grok.Context):
    pass


class Master(Layout):
    grok.name('master')
    grok.context(Cat)


class Utils(Page):
    grok.context(Interface)

    def render(self):
        return "<p>A purring cat</p>"


class FormUtils(Form):
    grok.context(Interface)

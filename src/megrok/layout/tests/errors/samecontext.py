"""
  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
  ...
  ConfigurationConflictError: Conflicting configuration actions
     For: ('adapter', (<InterfaceClass zope.publisher.interfaces.browser.IDefaultBrowserLayer>, <InterfaceClass zope.interface.Interface>), <InterfaceClass megrok.layout.interfaces.ILayout>)
"""

import grokcore.component as grok
from megrok.layout import Layout
from zope.interface import Interface


class MyLayout(Layout):
    grok.context(Interface)


class MyOtherLayout(Layout):
    grok.context(Interface)

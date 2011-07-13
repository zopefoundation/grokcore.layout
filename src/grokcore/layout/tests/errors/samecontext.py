"""
  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
  ...
  ConfigurationConflictError: Conflicting configuration actions
     For: ('adapter', (<InterfaceClass zope.publisher.interfaces.browser.IDefaultBrowserLayer>, <InterfaceClass zope.interface.Interface>), <InterfaceClass grokcore.layout.interfaces.ILayout>)
"""

import grokcore.component as grok
from grokcore.layout import Layout
from zope.interface import Interface


class MyLayout(Layout):
    grok.context(Interface)


class MyOtherLayout(Layout):
    grok.context(Interface)

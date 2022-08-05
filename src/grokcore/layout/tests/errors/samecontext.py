"""
  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
  ...
  zope.configuration.config.ConfigurationConflictError: \
  Conflicting configuration actions For: ('adapter', \
  (<InterfaceClass zope.publisher.interfaces.browser.IDefaultBrowserLayer>, \
  <InterfaceClass zope.interface.Interface>), \
  <InterfaceClass grokcore.layout.interfaces.ILayout>)

"""

import grokcore.component as grok
from zope.interface import Interface

from grokcore.layout import Layout


class MyLayout(Layout):
    grok.context(Interface)


class MyOtherLayout(Layout):
    grok.context(Interface)

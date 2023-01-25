"""
  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
  ...
  zope.configuration.config.ConfigurationExecutionError: \
  martian.error.GrokError: Layout \
  <class 'grokcore.layout.tests.errors.norenderortemplatelayout.MyLayout'> \
  has no associated template or 'render' method...

"""

import grokcore.component as grok
from zope.interface import Interface

from grokcore.layout import Layout


class MyLayout(Layout):
    grok.context(Interface)

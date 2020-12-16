"""
  >>> grok.testing.grok(__name__)  # doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
  ...
  zope.configuration.config.ConfigurationExecutionError: \
  martian.error.GrokError: Layout \
  <class 'grokcore.layout.tests.errors.norenderortemplatelayout.MyLayout'> \
  has no associated template or 'render' method...

"""

import grokcore.component as grok
from grokcore.layout import Layout
from zope.interface import Interface


class MyLayout(Layout):
    grok.context(Interface)

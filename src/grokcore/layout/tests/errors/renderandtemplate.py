"""
  # PY2 - remove '+IGNORE_EXCEPTION_DETAIL'  when dropping Python 2 support:
  >>> grok.testing.grok(__name__)  # doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
  ...
  zope.configuration.config.ConfigurationExecutionError: \
  martian.error.GrokError: Multiple possible ways to render layout \
  <class 'grokcore.layout.tests.errors.renderandtemplate.MyLayout'>. It has \
  both a 'render' method as well as an associated template...

"""

import grokcore.component as grok
from zope.interface import Interface

from grokcore.layout import Layout


class MyLayout(Layout):
    grok.context(Interface)

    def render(self):
        return ""

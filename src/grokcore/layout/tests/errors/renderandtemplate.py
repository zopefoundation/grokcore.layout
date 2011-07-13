"""
  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
  ...
  ConfigurationExecutionError: <class 'martian.error.GrokError'>: Multiple possible ways to render layout <class 'grokcore.layout.tests.errors.renderandtemplate.MyLayout'>. It has both a 'render' method as well as an associated template.
  in:
  <BLANKLINE>
"""

import grokcore.component as grok
from grokcore.layout import Layout
from zope.interface import Interface


class MyLayout(Layout):
    grok.context(Interface)

    def render(self):
        return ""

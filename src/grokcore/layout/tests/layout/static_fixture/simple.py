import grokcore.component as grok
from grokcore.layout import Layout

class Dummy(grok.Context):
    pass


class LayoutWithResources(Layout):

    def render(self):
        return ""

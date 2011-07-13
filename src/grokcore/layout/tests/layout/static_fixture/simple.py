import grokcore.component as grok
from megrok.layout import Layout

class Dummy(grok.Context):
    pass


class LayoutWithResources(Layout):

    def render(self):
        return ""

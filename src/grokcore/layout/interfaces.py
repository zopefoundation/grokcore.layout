# -*- coding: utf-8 -*-

from grokcore.view import interfaces
from zope.interface import Interface


class ILayout(Interface):
    """Layout view.
    """


class IPage(interfaces.IGrokView):
    """A view using a layout to render itself.
    """

    def content():
        """Give you back the result of your Page to be included inside
        the layout.
        """

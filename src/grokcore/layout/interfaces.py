# -*- coding: utf-8 -*-

from grokcore.view import interfaces
from zope.interface import Interface, Attribute


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


class IBaseClasses(Interface):
    Page = Attribute("Base class for a layout page.")

    Layout = Attribute("Base class for layout.")

    FormPage = Attribute("Base class for form page.")

    AddFormPage = Attribute("Base class for add form page.")

    EditFormPage = Attribute("Base class for edit form page.")

    DisplayFormPage = Attribute("Base class for diplay form layout.")

    UnauthorizedPage = Attribute("Base class for unauthorized page.")

    NotFoundPage = Attribute("Base class for not found page.")

    ExceptionPage = Attribute("Base class for exception page.")


class IGrokcoreLayoutAPI(IBaseClasses):
    """Grokcore layout API.
    """
    layout = Attribute("Directive used to specify layout on a page.")

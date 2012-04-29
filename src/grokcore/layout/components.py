import os

from grokcore.layout.interfaces import IPage, ILayout
from zope.interface import Interface
from zope.publisher.publish import mapply

import grokcore.component as grok
import grokcore.formlib
import grokcore.view
import zope.component
import zope.errorview.browser
import zope.interface.common.interfaces
import zope.publisher.interfaces
import zope.security.interfaces


class Layout(grokcore.view.ViewSupport):
    """A layout object.
    """
    grok.baseclass()
    grok.implements(ILayout)

    def __init__(self, request, context):
        self.context = context
        self.request = request
        self.view = None

        static_name = getattr(self, '__static_name__', None)
        if static_name is not None:
            self.static = zope.component.queryAdapter(
                self.request,
                Interface,
                name=static_name)
        else:
            self.static = None

    def default_namespace(self):
        namespace = {}
        namespace['view'] = self.view
        namespace['layout'] = self
        namespace['static'] = self.static
        namespace['context'] = self.context
        namespace['request'] = self.request
        return namespace

    def namespace(self):
        return {}

    def update(self):
        pass

    def _render_template(self):
        return self.template.render(self)

    def render(self):
        return self._render_template()

    render.base_method = True

    def __call__(self, view):
        self.view = view
        self.update()
        return self.render()


class LayoutAware(object):
    """A mixin to make views aware of layouts.
    """
    grok.baseclass()

    layout = None

    def __call__(self):
        self.layout = zope.component.getMultiAdapter(
            (self.request, self.context), ILayout)
        mapply(self.update, (), self.request)
        if self.request.response.getStatus() in (302, 303):
            # A redirect was triggered somewhere in update().  Don't
            # continue rendering the template or doing anything else.
            return
        return self.layout(self)

    def default_namespace(self):
        namespace = super(LayoutAware, self).default_namespace()
        namespace['layout'] = self.layout
        return namespace

    def content(self):
        template = getattr(self, 'template', None)
        if template is not None:
            return self._render_template()
        return mapply(self.render, (), self.request)


class LayoutAwareFormPage(LayoutAware):
    """A mixin to make form aware of layouts.
    """
    def __call__(self):
        """Calls update and returns the layout template which calls render.
        """
        mapply(self.update, (), self.request)
        if self.request.response.getStatus() in (302, 303):
            # A redirect was triggered somewhere in update().  Don't
            # continue rendering the template or doing anything else.
            return
        # update_form() is what make a layout-aware form different from
        # 'regular" layout-aware component.
        self.update_form()
        if self.request.response.getStatus() in (302, 303):
            return
        self.layout = zope.component.getMultiAdapter(
            (self.request, self.context), ILayout)
        return self.layout(self)


class Page(LayoutAware, grokcore.view.View):
    """A view class.
    """
    grok.baseclass()
    grok.implements(IPage)


class ExceptionPage(
        LayoutAware,
        zope.errorview.browser.ExceptionView,
        grokcore.view.View
        ):
    grok.context(zope.interface.common.interfaces.IException)
    grok.baseclass()


class NotFoundPage(
        LayoutAware,
        zope.errorview.browser.NotFoundView,
        grokcore.view.View
        ):
    grok.context(zope.publisher.interfaces.INotFound)
    grok.baseclass()


class UnauthorizedPage(
        LayoutAware,
        zope.errorview.browser.UnauthorizedView,
        grokcore.view.View
        ):
    grok.context(zope.security.interfaces.IUnauthorized)
    grok.baseclass()


# Default forms for form without the html and body tags
default_form_template = grokcore.view.PageTemplateFile(
    os.path.join('templates', 'default_edit_form.pt'))
default_form_template.__grok_name__ = 'default_edit_form'

default_display_template = grokcore.view.PageTemplateFile(
    os.path.join('templates', 'default_display_form.pt'))
default_display_template.__grok_name__ = 'default_display_form'

grokcore.view.templatedir('templates')


class FormPage(LayoutAwareFormPage, grokcore.formlib.Form):
    """A form base class.
    """
    grok.baseclass()
    template = default_form_template


class AddFormPage(LayoutAwareFormPage, grokcore.formlib.AddForm):
    """Base add form.
    """
    grok.baseclass()
    template = default_form_template


class EditFormPage(LayoutAwareFormPage, grokcore.formlib.EditForm):
    """Base edit form.
    """
    grok.baseclass()
    template = default_form_template


class DisplayFormPage(LayoutAwareFormPage, grokcore.formlib.DisplayForm):
    """Base display form.
    """
    grok.baseclass()
    template = default_display_template

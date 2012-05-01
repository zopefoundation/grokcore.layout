"""
    >>> from zope.component import getMultiAdapter
    >>> from zope.publisher.browser import TestRequest
    >>> view = getMultiAdapter((Exception(), TestRequest()), name='index')
    >>> import grokcore.layout
    >>> isinstance(view, grokcore.layout.ExceptionPage)
    True
    >>> print view.render()
    A system error occurred.
    >>> print view()
    <html>
    <body>
    <div class="layout">A system error occurred.</div>
    </body>
    </html>

    >>> from zope.security.interfaces import Unauthorized
    >>> class MockPrincipal(object):
    ...     id = 'mock principal'
    >>> request = TestRequest()
    >>> request.setPrincipal(MockPrincipal())
    >>> errorpage = getMultiAdapter((Unauthorized(), request), name='index')
    >>> print errorpage()
    <html>
    <body>
    <div class="layout">Access to the requested resource is forbidden.</div>
    </body>
    </html>

    >>> from zope.publisher.interfaces import NotFound
    >>> request = TestRequest()
    >>> errorpage = getMultiAdapter(
    ...     (NotFound(None, request), request), name='index')
    >>> print errorpage()
    <html>
    <body>
    <div class="layout">The requested resource can not be found.</div>
    </body>
    </html>

"""
import grokcore.component as grok

from grokcore.view import templatedir
from grokcore.layout import Layout, ExceptionPage, NotFoundPage, UnauthorizedPage

templatedir('templates')

class Master(Layout):
    grok.name('master')
    grok.context(Exception)

class MyExceptionPage(ExceptionPage):
    grok.name('index')

class MyUnauthorizedPage(UnauthorizedPage):
    grok.name('index')

class MyNotFoundPage(NotFoundPage):
    grok.name('index')

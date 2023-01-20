import zope.component
from zope.component.testlayer import ZCMLFileLayer
from zope.container.interfaces import ISimpleReadContainer
from zope.container.traversal import ContainerTraversable
from zope.interface import Interface
from zope.interface.interfaces import IComponentLookup
from zope.publisher.interfaces import IRequest
from zope.session.http import CookieClientIdManager
from zope.session.interfaces import IClientId
from zope.session.interfaces import IClientIdManager
from zope.session.interfaces import ISession
from zope.session.interfaces import ISessionDataContainer
from zope.session.session import ClientId
from zope.session.session import PersistentSessionDataContainer
from zope.session.session import Session
from zope.site.folder import rootFolder
from zope.site.site import LocalSiteManager
from zope.site.site import SiteManagerAdapter
from zope.traversing.interfaces import ITraversable
from zope.traversing.testing import setUp as traversingSetUp


class GrokcoreLayoutLayer(ZCMLFileLayer):

    def setUp(self):
        ZCMLFileLayer.setUp(self)

        # Set up site manager adapter
        zope.component.provideAdapter(
            SiteManagerAdapter, (Interface,), IComponentLookup)

        # Set up traversal
        traversingSetUp()
        zope.component.provideAdapter(
            ContainerTraversable, (ISimpleReadContainer,), ITraversable)

        # Session
        zope.component.provideAdapter(ClientId, (IRequest,), IClientId)
        zope.component.provideAdapter(Session, (IRequest,), ISession)
        zope.component.provideUtility(
            CookieClientIdManager(), IClientIdManager)
        sdc = PersistentSessionDataContainer()
        zope.component.provideUtility(sdc, ISessionDataContainer, '')

        # Set up site
        site = rootFolder()
        site.setSiteManager(LocalSiteManager(site))
        zope.component.hooks.setSite(site)

        return site

    def tearDown(self):
        ZCMLFileLayer.tearDown(self)
        zope.component.hooks.resetHooks()
        zope.component.hooks.setSite()

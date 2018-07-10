from Products.Five.browser import BrowserView
from plone import api


class UpdateAlbums(BrowserView):
    def __call__(self, *args, **kw):
        data = ['update albums']
        for brain in api.content.find(portal_type='Folder'):
            if brain.getObject().getLayout() == 'album_view':
                folder = brain.getObject()
                folder.setLayout('prettyPhoto_album_view')
                folder.indexObject()
                data.append('%s <a href="%s">%s</a> Fixed' % (
                            brain.Title, brain.getURL(), brain.getURL()))
        return '<br />'.join(data)

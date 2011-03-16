from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IPropertiesTool

# Properties are defined here, because if they are defined in
# propertiestool.xml, all properties are re-set the their initial state if you
# reinstall product in the quickinstaller.

_PROPERTIES = [
    dict(name='speed', type_='string', value='normal'),
    dict(name='opacity', type_='string', value='0.80'),
    dict(name='show_title', type_='boolean', value=True),
    dict(name='counter_sep', type_='string', value='/'),
    dict(name='theme', type_='string', value='light_rounded'),
    dict(name='autoplay', type_='boolean', value=True),
    dict(name='iframe_width', type_='string', value='75%'),
    dict(name='iframe_height', type_='string', value='75%'),
]

def configureKupu(kupu):

    paragraph_styles = list(kupu.getParagraphStyles())

    new_styles = [
        ('prettyPhoto', 'prettyPhoto Link|a'),
        ('prettyPhotoIframe', 'prettyPhoto Iframe Link|a'),
    ]
    to_add = dict(new_styles)

    for style in paragraph_styles:
        css_class = style.split('|')[-1]
        if css_class in to_add:
            del to_add[css_class]

    if to_add:
        paragraph_styles += ['%s|%s' % (v, k) for k, v in new_styles if \
                             k in to_add]
        kupu.configure_kupu(parastyles=paragraph_styles)

def import_various(context):
    if not context.readDataFile('collective.prettyphoto.txt'):
        return

    site = context.getSite()

    # skip kupu configuration on sites that don't have kupu installed
    kupu = getToolByName(site, 'kupu_library_tool', None)
    if kupu is not None:
        configureKupu(kupu)

    # Define portal properties
    ptool = getToolByName(site, 'portal_properties')
    props = ptool.prettyphoto_properties

    for prop in _PROPERTIES:
        if not props.hasProperty(prop['name']):
            props.manage_addProperty(prop['name'], prop['value'],
                                     prop['type_'])

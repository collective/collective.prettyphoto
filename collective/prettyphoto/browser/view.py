from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


class JavaScript(BrowserView):

    @property
    def prettyphoto_properties(self):
        properties_tool = getToolByName(self.context, 'portal_properties')
        return getattr(properties_tool, 'prettyphoto_properties', None)

    def __call__(self, request=None, response=None):
        """Returns global configuration for prettyPhoto taken from
           portal_properties."""
        self.request.response.setHeader("Content-type", "text/javascript")

        return """jq(document).ready(function(){
            jq(document).ready(function(){
                // add rel tag for all links with class 'prettyPhoto'
                jq("a.prettyPhoto").attr({"rel": "prettyPhoto"});

                // add iframe attributes for all links with class 'prettyPhotoIframe'
                jq("a.prettyPhotoIframe").attr("href", function() {
                    return this.href + "?iframe=true&width=%(iframe_width)s&height=%(iframe_height)s";
                }).attr({"rel": "prettyPhoto"});

                // enable prettyPhoto
                jq("a[rel^='prettyPhoto']").prettyPhoto({
                    animationSpeed: '%(speed)s', /* fast/slow/normal */
                    opacity: %(opacity)s, /* Value between 0 and 1 */
                    showTitle: %(show_title)s, /* true/false */
                    counter_separator_label: '%(counter_sep)s', /* The separator for the gallery counter 1 "of" 2 */
                    theme: '%(theme)s',
                    autoplay: %(autoplay)s, /* Automatically start videos: True/False */
                });
            });
        });
        """ % dict(speed = getattr(self.prettyphoto_properties, 'speed', 'normal'),
                   opacity = getattr(self.prettyphoto_properties, 'opacity', '0.80'),
                   show_title = getattr(self.prettyphoto_properties, 'show_title', True) and 'true' or 'false',
                   counter_sep = getattr(self.prettyphoto_properties, 'counter_sep', '/'),
                   theme = getattr(self.prettyphoto_properties, 'theme', 'light_rounded'),
                   autoplay = getattr(self.prettyphoto_properties, 'autoplay', True) and 'true' or 'false',
                   iframe_width = getattr(self.prettyphoto_properties, 'iframe_width', '75%'),
                   iframe_height = getattr(self.prettyphoto_properties, 'iframe_width', '75%'),
              )

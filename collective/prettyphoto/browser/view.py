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

        social_tools = getattr(self.prettyphoto_properties, 'social_tools', '')


        slideshowInterval = getattr(self.prettyphoto_properties, 'slideshow', 0)
        autoplaySlideshow = getattr(self.prettyphoto_properties, 'autoplay_slideshow', False)
        if slideshowInterval <= 0:
            # automatically starting the slideshow does only make sense if the interval is greater than 0
            autoplaySlideshow = False

        return """\
        var plonePrettyPhoto = {};
        (function($) {
            plonePrettyPhoto.enable = function () {
                // add rel tag for all links with class 'prettyPhoto'
                $("a.prettyPhoto").attr({"rel": "prettyPhoto"});

                // add iframe attributes for all links with class 'prettyPhotoIframe'
                $("a.prettyPhotoIframe").attr("href", function() {
                    return this.href + "?iframe=true&width=%(iframe_width)s&height=%(iframe_height)s";
                }).attr({"rel": "prettyPhoto"});

                // enable prettyPhoto
                $("a[rel^='prettyPhoto']").prettyPhoto({
                    animation_speed: '%(speed)s', /* fast/slow/normal */
                    opacity: %(opacity)s, /* Value between 0 and 1 */
                    show_title: %(show_title)s, /* true/false */
                    counter_separator_label: '%(counter_sep)s', /* The separator for the gallery counter 1 "of" 2 */
                    theme: '%(theme)s',
                    autoplay: %(autoplay)s, /* Automatically start videos: true/false */
                    autoplay_slideshow: %(autoplay_slideshow)s,
                    slideshow: %(slideshow)s, /* false OR interval time in ms */
                    overlay_gallery: %(overlay_gallery)s, /* If set to true, a gallery will overlay the fullscreen image on mouse over */
                    social_tools: %(social_tools)s, /* html markup for social tool icons */
                    deeplinking: %(deeplinking)s, /* allow prettyphoto to rewrite url for direktlinking to an image */
                    markup: %(markup)s
                });
            };

            $(function() {
                // enable prettyPhoto on document load
                plonePrettyPhoto.enable();
            });
        })(jQuery);
        """ % dict(speed=getattr(self.prettyphoto_properties, 'speed', 'normal'),
                   opacity=getattr(self.prettyphoto_properties, 'opacity', '0.80'),
                   show_title=getattr(self.prettyphoto_properties, 'show_title', True) and 'true' or 'false',
                   counter_sep=getattr(self.prettyphoto_properties, 'counter_sep', '/'),
                   theme=getattr(self.prettyphoto_properties, 'theme', 'light_rounded'),
                   autoplay=getattr(self.prettyphoto_properties, 'autoplay', True) and 'true' or 'false',
                   iframe_width=getattr(self.prettyphoto_properties, 'iframe_width', '75%'),
                   iframe_height=getattr(self.prettyphoto_properties, 'iframe_height', '75%'),
                   overlay_gallery=getattr(self.prettyphoto_properties, 'overlay_gallery', False) and 'true' or 'false',
                   slideshow=slideshowInterval or 'false',
                   autoplay_slideshow=autoplaySlideshow  and 'true' or 'false',
                   social_tools=social_tools and "'%s'" % social_tools or 'false',
                   deeplinking=getattr(self.prettyphoto_properties, 'deeplinking', False) and 'true' or 'false',
                   markup=self.markup() or 'undefined',
              )

    def markup(self):
        """subclasses can overwrite this to provide another default markup
        for the overlay.

        eg:
        return '''"<div class="pp_pic_holder"> \\
            <div class="pp_top"> \\
            ..." '''
        """
        return None

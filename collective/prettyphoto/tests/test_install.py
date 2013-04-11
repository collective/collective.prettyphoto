# -*- coding: utf-8 -*-
from collective.prettyphoto.testing import COLLECTIVE_PRETTYPHOTO_INTEGRATION

import unittest2 as unittest


class InstallationTestCase(unittest.TestCase):

    layer = COLLECTIVE_PRETTYPHOTO_INTEGRATION

    def setUp(self):
        self.portal = self.layer['portal']

    def test_css_registered(self):
        css_registry = self.portal['portal_css']
        stylesheets_ids = css_registry.getResourceIds()
        self.assertIn('++resource++prettyPhoto.css', stylesheets_ids)

    def test_js_registered(self):
        js_registry = self.portal['portal_javascripts']
        javascript_ids = js_registry.getResourceIds()
        self.assertIn('++resource++jquery.prettyPhoto.js', javascript_ids)
        self.assertIn('prettyPhoto.js', javascript_ids)

# -*- coding: utf-8 -*-
"""Test the AD54Elements multisearch viewlet."""
import unittest2 as unittest
from BeautifulSoup import BeautifulSoup
from .base import AD54ELEMENTS_FUNCTIONAL_TESTING


class LogoViewletTestCase(unittest.TestCase):
    layer = AD54ELEMENTS_FUNCTIONAL_TESTING

    def test_psu_anchor(self):
        from Products.AD54Elements.browser.viewlets import LogoViewlet
        context = self.layer['portal']
        request = self.layer['request']
        viewlet = LogoViewlet(context, request, None, None)
        viewlet.update()
        results = viewlet.render()
        
        # Parse the results into soup
        html = BeautifulSoup(results)

        anchor = html.find('a', attrs={'title': 'Penn State'})['href']
        expected_anchor = u'http://www.psu.edu'
        self.assertEquals(anchor, expected_anchor)


class FooterViewletTestCase(unittest.TestCase):
    layer = AD54ELEMENTS_FUNCTIONAL_TESTING

    def test_legal_statements_anchor(self):
        from Products.AD54Elements.browser.viewlets import FooterViewlet
        context = self.layer['portal']
        request = self.layer['request']
        viewlet = FooterViewlet(context, request, None, None)
        viewlet.update()
        results = viewlet.render()

        # Parse the results into soup
        html = BeautifulSoup(results)

        statements = html.findAll('a', attrs={'href': 'http://www.psu.edu/ur/legal.html'})
        self.assertGreaterEqual(len(statements), 1)



class FaviconViewletTestCase(unittest.TestCase):
    layer = AD54ELEMENTS_FUNCTIONAL_TESTING

    def setUp(self):
        from Products.AD54Elements.browser.viewlets import FaviconViewlet
        context = self.layer['portal']
        request = self.layer['request']
        viewlet = FaviconViewlet(context, request, None, None)

        from Products.AD54Elements.interfaces import IAD54ElementsLayer
        from zope.interface import directlyProvides
        directlyProvides(context, IAD54ElementsLayer)
        
        viewlet.update()
        results = viewlet.render()
        # Parse the results into soup
        html = BeautifulSoup(results)
        
        rels = {}
        for rel in html.findAll('link'):
            rels[rel['rel']] = rel['href']

        self.rels = rels

    def test_favicon(self):
        si = u'shortcut icon'
        self.assertTrue(si in self.rels)
        self.assertIn(u'++resource++images/favicon.ico', self.rels[si])

    def test_touchicon(self):
        ati = u'apple-touch-icon'
        self.assertTrue(ati in self.rels)
        self.assertIn(u'++resource++images/touch_icon.png', self.rels[ati])


class MultisearchViewletTestCase(unittest.TestCase):
    layer = AD54ELEMENTS_FUNCTIONAL_TESTING

    def test_default_options(self):
        # Initialize the viewlet
        from Products.AD54Elements.browser.viewlets import MultiSearchViewlet
        context = self.layer['portal']
        request = self.layer['request']
        viewlet = MultiSearchViewlet(context, request, None, None)
        viewlet.update()
        options = viewlet.getSearchOptions()
        # Test the results...
        expected_options = [
            {'selected': True, 'description': 'Search This Site', 'key': 'thisSite'},
            {'selected': False, 'description': 'Search Google', 'key': 'google'},
            {'selected': False, 'description': 'Search Penn State Web', 'key': 'PSUweb'},
            {'selected': False, 'description': 'Search Penn State People', 'key': 'PSUpeople'},
            {'selected': False, 'description': 'Search Penn State Accounts', 'key': 'PSUemail'},
            {'selected': False, 'description': 'Search Penn State Departments', 'key': 'PSUdept'},
            ]
        self.assertEqual(options, expected_options)

    @unittest.skip("Unable to test this at this time.")
    def test_without_options(self):
        pass

    @unittest.skip("Unable to test this at this time.")
    def test_new_options(self):
        pass

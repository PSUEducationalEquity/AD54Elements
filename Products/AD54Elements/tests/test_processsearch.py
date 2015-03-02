# -*- coding: utf-8 -*-
"""Test the AD54Elements process search logic used by the multisearch viewlet."""
import unittest2 as unittest
from .base import AD54ELEMENTS_FUNCTIONAL_TESTING


class ProcessSearchTestCase(unittest.TestCase):
    layer = AD54ELEMENTS_FUNCTIONAL_TESTING

    def test_for_redirect(self):
        context = self.layer['portal']
        request = self.layer['request']
        # Set up the form values
        request['choice'] = 'google'
        request['searchString'] = "Welcome"
        # Initialize the browser view
        from Products.AD54Elements.browser.processsearch import ProcessSearch
        view = ProcessSearch(context, request)
        view()
        # Check for the redirect
        response = request.RESPONSE
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.headers, {'location': 'http://google.com/search?q=Welcome'})

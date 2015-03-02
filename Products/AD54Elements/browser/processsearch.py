from urllib import quote_plus
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

_defaultSearch = 'search?SearchableText=%s'

class ProcessSearch(BrowserView):
    """I need to put a doctest in here sometime soon."""
    
    def __call__(self):
        """"""
        ad54_props = getToolByName(getToolByName(self.context, 'portal_properties'), 'ad54elements_properties')

        keys = ad54_props.getProperty('searchKeys')
        links = ad54_props.getProperty('searchLinks')
        default = ad54_props.getProperty('searchDefault')

        # build a list of searches, if possible
        searches = {}
        if keys is not None and links is not None:
            for index in range(0,min(len(keys),len(links))):
                searches[keys[index]] = links[index]

        # pick a default search in case the key is missing
        defaultSearch = searches.get(default, _defaultSearch)

        req = self.context.REQUEST
        return req.RESPONSE.redirect(searches.get(req['choice'], defaultSearch) % quote_plus(req['searchString']))

# -*- coding: utf-8 -*-

#import logging
#from Acquisition import aq_inner
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone import api
from DateTime import DateTime
 

        
class Manifest(BrowserView):
    """List of urls to cache"""
    
    def __call__(self):
        urls = '#Cached urls, date:' + (str(DateTime()))[0:16] +'\n'
        catalog = api.portal.get_tool(name='portal_catalog')
        all_brains = catalog.searchResults()
        for brain in all_brains:
            urls += (brain.getURL())
            urls +="\n"
             
        return """CACHE MANIFEST
# Explicitly cached entries
/++theme++medialog.mobilethemeWessel/assets/authoring.css 
/++theme++medialog.mobilethemeWessel/assets/IcoMoon/Icons/png/32px/mail4.png
/++theme++medialog.mobilethemeWessel/assets/IcoMoon/Icons/png/32px/newspaper.png
/++theme++medialog.mobilethemeWessel/assets/IcoMoon/Icons/png/32px/phone.png
/++theme++medialog.mobilethemeWessel/assets/images/add.png
/++theme++medialog.mobilethemeWessel/assets/images/addbutton.png
/++theme++medialog.mobilethemeWessel/assets/images/bubble.png
/++theme++medialog.mobilethemeWessel/assets/images/call.png
/++theme++medialog.mobilethemeWessel/assets/images/gear.png
/++theme++medialog.mobilethemeWessel/assets/images/home.png
/++theme++medialog.mobilethemeWessel/assets/images/info.png
/++theme++medialog.mobilethemeWessel/assets/images/mail.png
/++theme++medialog.mobilethemeWessel/assets/images/navigation.png
/++theme++medialog.mobilethemeWessel/assets/images/quotes.png
/++theme++medialog.mobilethemeWessel/assets/invisibles.css
/++theme++medialog.mobilethemeWessel/assets/mobileWessel.css 
/++theme++medialog.mobilethemeWessel/assets/navigation.css 
/++theme++medialog.mobilethemeWessel/assets/reset.css 
/++theme++medialog.mobilethemeWessel/assets/slider.min.js
/contact-info
#/sitemap
%s

# offline.html will be displayed if the user is offline
#FALLBACK:
#/ /++theme++medialog.mobilethemeWessel/offline.html

# All other resources (e.g. sites) require the user to be online. 
NETWORK:
*

# Additional resources to cache
#CACHE:
#get sitemap here, maybe
""" %(urls)


        return printed
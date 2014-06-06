#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ha.Minh'
SITENAME = u"Ha.Minh's Blog"
SITEURL = 'http://minhhh.github.io'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          )

# Social widget
SOCIAL = (
          ('Twitter', 'https://twitter.com/utsace'),
          )

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = ('Articles')
MD_EXTENSIONS = ['codehilite','extra']
MARKUP = ('rst', 'md')
ARTICLE_EXCLUDES = ('pages',)
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'

THEME = "themes/gum"
STATIC_PATHS = ['images', 'js', 'css']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = False

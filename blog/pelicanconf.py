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
# SOCIAL = (
#           # ('Twitter', 'https://twitter.com/utsace'),
#           )
SOCIAL =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          )

GITHUB_URL = 'https://github.com/minhhh'
TWITTER_URL = 'https://twitter.com/utsace'
FACEBOOK_URL = 'https://www.facebook.com/minh.ha.hanoi'
GOOGLEPLUS_URL = 'https://plus.google.com/u/0/104727235342101204530/about/p/pub'

# Pages
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = ('Programming')
MD_EXTENSIONS = ['codehilite','extra']
MARKUP = ('rst', 'md')
ARTICLE_EXCLUDES = ('pages',)

# Url
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_LANG_URL = '{pages/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

# Archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Themes
THEME = "pelican-themes/gum"
STATIC_PATHS = ['images', 'js', 'css']

# Analytics
GOOGLE_ANALYTICS = 'UA-50796592-2'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = False

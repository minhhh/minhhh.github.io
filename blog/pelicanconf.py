#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Huy Minh Ha'
SITENAME = u"Huy Minh Ha"
SITEURL = 'https://minhhh.github.io'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PLUGINS = [
    'pelican_gist',
    'pelican_git',
]

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          )

# Pages
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = ('Programming')
MD_EXTENSIONS = ['codehilite','extra']
MARKUP = ('rst', 'md')
ARTICLE_EXCLUDES = ('pages',)

# Url
# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_URL = 'posts/{slug}'
ARTICLE_LANG_URL = 'posts/{slug}-{lang}'
PAGE_URL = 'pages/{slug}'
PAGE_LANG_URL = '{pages/{slug}-{lang}'
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{slug}-{lang}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

# Archive
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Themes
THEME = "pelican-themes/voidy-bootstrap"
STATIC_PATHS = ['images', 'js', 'css']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = False

# VoidyBootstrap
SITESUBTITLE ='Software development, Tech and other stuff'

STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

SIDEBAR = "sidebar.html"

# Social widget
SOCIAL = (
        #('Google+', 'https://plus.google.com/u/0/104727235342101204530/about/p/pub',
        # 'fa fa-google-plus-square fa-fw'),
        ('Twitter', 'https://twitter.com/utsace',
         'fa fa-twitter-square fa-fw'),
        ('Facebook', 'https://www.facebook.com/minh.ha.hanoi',
         'fa fa-facebook-square fa-fw'),
        ('GitHub', 'https://github.com/minhhh',
         'fa fa-github-square fa-fw'),
        )

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'webdancer'
SITENAME = u"AI's bazaar"
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Scturtle', 'http://scturtle.me/'),
          )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/seaslee'),
        ('Github', 'http://github.com/seaslee'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Formatting for dates

DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first

NEWEST_FIRST_ARCHIVES = False

# Specify theme

#THEME = "themes/bootstrap2"

# Plugins

PLUGIN_PATH = "plugins/"
PLUGINS = ['latex', 'summary']

# Only use LaTeX for selected articles

#LATEX = 'article'

#disq
DISQUS_SITENAME = 'webdancer'

STATIC_PATHS = ['images/']

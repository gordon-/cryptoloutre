#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Cryptoloutre'
SITENAME = u'Cryptoloutre'
SITEURL = 'http://cryptolout.re'
FILENAME_METADATA = '(?P<slug>.*)'
ARTICLE_URL = '{category.slug}/{slug}.html'
ARTICLE_SAVE_AS = '{category.slug}/{slug}.html'

MENUITEMS = [('Accueil', '/')]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['files', 'images']

DEFAULT_PAGINATION = 5
THEME="template"

OUTPUT_SOURCES = True

MD_EXTENSIONS = ['codehilite', 'extra', 'headerid']

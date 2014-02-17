# Hari Ganesan 1/8/14
# defs file for fried-python

import os

BLOG_NAME = 'fried-python'
CANONICAL_BLOG_URL = 'http://fried-python.appspot.com/'
BLOG_OWNER = 'Hari Ganesan'

TEMPLATE_SUBDIR = 'templates'

TAG_URL_PATH = 'tag'
DATE_URL_PATH = 'date'
ARTICLE_URL_PATH = 'id'
MEDIA_URL_PATH = 'static'
ATOM_URL_PATH = 'atom'
RSS2_URL_PATH = 'rss2'
ARCHIVE_URL_PATH = 'archive'

MAX_ARTICLES_PER_PAGE = 5
TOTAL_RECENT = 10

_server_software = os.environ.get('SERVER_SOFTWARE','').lower()
if _server_software.startswith('goog'):
    ON_GAE = True
else:
    ON_GAE = False
del _server_software

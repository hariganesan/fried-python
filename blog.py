# Hari Ganesan 1/8/14
# blog file for fried-python
# created by Hari Ganesan 1/2014
# main app for briefme-web

import os
import webapp2
import logging
import json

from google.appengine.ext.webapp import template
from google.appengine.ext import db

# used for template subdirectory
import defs
from models import *
import handlers


####################
# Models and objects
####################

# mail info model for mailing list
class MailInfo(db.Model):
	name = db.StringProperty()
	email = db.StringProperty()

	@classmethod
	def get_list(cls):
		return cls.query().order(cls.name)

# Convenience class for storing and sorting year/month counts.
class DateCount(object):
	def __init__(self, date, count):
		self.date = date
		self.count = count

	def __cmp__(self, other):
		return cmp(self.date, other.date)

	def __hash__(self):
		return self.date.__hash__()

	def __str__(self):
		return '%s(%d)' % (self.date, self.count)

	def __repr__(self):
		return '<%s: %s>' % (self.__class__.__name__, str(self))

# Convenience class for storing and sorting tags and counts.
class TagCount(object):
	def __init__(self, tag, count):
		self.css_class = ""
		self.count = count
		self.tag = tag

#########################
# Blog Handlers
#########################

# Handles requests to display the front (or main) page of the blog.
class FrontPageHandler(handlers.AbstractPageHandler):
	def get(self):
		articles = Article.published()
		if len(articles) > defs.MAX_ARTICLES_PER_PAGE:
			articles = articles[:defs.MAX_ARTICLES_PER_PAGE]

		self.response.out.write(self.render_articles(articles,
													 self.request,
													 self.get_recent()))

# Handles requests to display a set of articles that have a
# particular tag.
class ArticlesByTagHandler(handlers.AbstractPageHandler):
	def get(self, tag):
		articles = Article.all_for_tag(tag)
		self.response.out.write(self.render_articles(articles,
													 self.request,
													 self.get_recent()))

# Handles requests to display a set of articles that were published
# in a given month.
class ArticlesForMonthHandler(handlers.AbstractPageHandler):
	def get(self, year, month):
		articles = Article.all_for_month(int(year), int(month))
		self.response.out.write(self.render_articles(articles,
													 self.request,
													 self.get_recent()))

# Handles requests to display a single article, given its unique ID.
# Handles nonexistent IDs.
class SingleArticleHandler(handlers.AbstractPageHandler):
	def get(self, id):
		article = Article.get(int(id))
		if article:
			template = 'show-articles.html'
			articles = [article]
			more = None
		else:
			template = 'not-found.html'
			articles = []

		self.response.out.write(self.render_articles(articles=articles,
													 request=self.request,
													 recent=self.get_recent(),
													 template_name=template))

# Handles requests to display the list of all articles in the blog.
class ArchivePageHandler(handlers.AbstractPageHandler):
	def get(self):
		articles = Article.published()
		self.response.out.write(self.render_articles(articles,
													 self.request,
													 [],
													 'archive.html'))

# Handles pages that aren't found.
class NotFoundPageHandler(handlers.AbstractPageHandler):
	def get(self):
		self.response.out.write(self.render_articles([],
													 self.request,
													 [],
													 'not-found.html'))

	# blog routes
app = webapp2.WSGIApplication(
	[('/', FrontPageHandler),
	 ('/tag/([^/]+)/*$', ArticlesByTagHandler),
	 ('/date/(\d\d\d\d)-(\d\d)/?$', ArticlesForMonthHandler),
	 ('/id/(\d+)/?$', SingleArticleHandler),
	 ('/archive/?$', ArchivePageHandler),
	 ('/.*$', NotFoundPageHandler)
	], debug=True)

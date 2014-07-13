# Hari Ganesan 12/21/13
# main file for fried-python

import os
import logging
import json

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
import webapp2

# used for template subdirectory
import defs
from models import *
import handlers

# spits a path to a request handler
def spitPath(self, path):
	fullPath = os.path.join(os.path.dirname(__file__), path)
	self.response.out.write(template.render(fullPath, {}))


#########################
# Static Handlers
#########################

# main routes to static pages
class MainPageHandler(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/index.html")

class PortfolioPageHandler(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/portfolio.html")

class AboutPageHandler(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/about.html")

class ColorsPageHandler(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/colors.html")

class ExtraPageHandler(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/extra.html")

class NotFoundPageHandler(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/notfound.html")

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
# class ArticlesByTagHandler(handlers.AbstractPageHandler):
# 	def get(self, tag):
# 		articles = Article.all_for_tag(tag)
# 		self.response.out.write(self.render_articles(articles,
# 													 self.request,
# 													 self.get_recent()))

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
		logging.info(len(articles))
		self.response.out.write(self.render_articles(articles,
													 self.request,
													 [],
													 'archive.html'))

app = webapp2.WSGIApplication([
	('/', MainPageHandler),
	('/portfolio', PortfolioPageHandler),
	('/about', AboutPageHandler),
	('/extra', ExtraPageHandler),
	('/colors', ColorsPageHandler),
	('/blog', FrontPageHandler),
	# ('/tag/([^/]+)/*$', ArticlesByTagHandler),
	('/date/(\d\d\d\d)-(\d\d)/?$', ArticlesForMonthHandler),
	('/(\d+)/?$', SingleArticleHandler),
	('/archive/?$', ArchivePageHandler),
	('/.*$', NotFoundPageHandler)
], debug=True)

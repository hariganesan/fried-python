# Hari Ganesan 12/21/13
# main file for fried-python

import os
import logging

import webapp2
from google.appengine.ext.webapp import template
import defs

# spits a path to a request handler
def spitPath(self, path):
	fullPath = os.path.join(os.path.dirname(__file__), path)
	logging.info(os.path.dirname(__file__))
	self.response.out.write(template.render(fullPath, {}))

# routes
class MainPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/index.html")

class PortfolioPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/portfolio.html")

class AboutPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/about.html")

class NotFoundPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/notfound.html")

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/portfolio', PortfolioPage),
	('/about', AboutPage),
	('/.*', NotFoundPage)
], debug=True)

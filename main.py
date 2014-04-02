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
		spitPath(self, "templates/main/index.html")

class PortfolioPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/portfolio.html")

class AboutPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/about.html")

class ColorsPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/colors.html")

class ExtraPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/extra.html")

class NotFoundPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "templates/main/notfound.html")

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/portfolio', PortfolioPage),
	('/about', AboutPage),
	('/extra', ExtraPage),
	('/colors', ColorsPage),
	('/.*', NotFoundPage)
], debug=True)

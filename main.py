import os
import webapp2
import logging

from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template

# spits a path to a request handler
def spitPath(self, path):
	fullPath = os.path.join(os.path.dirname(__file__), path)
	logging.info(os.path.dirname(__file__))
	self.response.out.write(template.render(fullPath, {}))

# routes
class MainPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "views/index.html")

class PortfolioPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "views/portfolio.html")

class BlogPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "views/blog.php")

class AboutPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "views/about.html")

class NotFoundPage(webapp2.RequestHandler):
	def get(self):
		spitPath(self, "views/notfound.html")

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/portfolio', PortfolioPage),
	('/blog', BlogPage),
	('/about', AboutPage),
	('/notfound', NotFoundPage)
], debug=True)

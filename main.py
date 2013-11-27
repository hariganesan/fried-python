import os
import webapp2
import logging

from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template

# webapp2 class
class MainPage(webapp2.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), "public_html/index.html")
		logging.info(os.path.dirname(__file__))
		self.response.out.write(template.render(path, {}))

app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)

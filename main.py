# Hari Ganesan 12/21/13
# main file for fried-python

import os

from google.appengine.ext.webapp import template
import webapp2

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
        spitPath(self, "templates/index.html")

class PortfolioPageHandler(webapp2.RequestHandler):
    def get(self):
        spitPath(self, "templates/portfolio.html")

class AboutPageHandler(webapp2.RequestHandler):
    def get(self):
        spitPath(self, "templates/about.html")

class ColorsPageHandler(webapp2.RequestHandler):
    def get(self):
        spitPath(self, "templates/colors.html")

class NotFoundPageHandler(webapp2.RequestHandler):
    def get(self):
        spitPath(self, "templates/notfound.html")


app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/portfolio', PortfolioPageHandler),
    ('/about', AboutPageHandler),
    ('/colors', ColorsPageHandler),
    ('/.*$', NotFoundPageHandler)
], debug=True)

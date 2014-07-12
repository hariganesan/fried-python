# created by Hari Ganesan 2/14/14
# fried-python blog base handlers

import os
import random
import logging

import webapp2
from google.appengine.ext.webapp import template

import defs
from models import *


# handler for all blog pages
class BlogRequestHandler(webapp2.RequestHandler):
	def get_template(self, template_name):
		return os.path.join(os.path.dirname(__file__), 
							defs.TEMPLATE_SUBDIR,
							template_name)

	# Render a template and write the output to ``self.response.out``.
	def render_template(self, template_name, template_vars):
		template_path = self.get_template(template_name)
		return template.render(template_path, template_vars)

# Abstract base class for all handlers in this module. Basically,
# this class exists to consolidate common logic.
class AbstractPageHandler(BlogRequestHandler):
	# Get tag counts and calculate tag cloud frequencies.
	# def get_tag_counts(self):
	# 	tag_counts = Article.get_all_tags()
	# 	result = []
	# 	if tag_counts:
	# 		maximum = max(tag_counts.values())

	# 		for tag, count in tag_counts.items():
	# 			tc = TagCount(tag, count)

	# 			# Determine the popularity of this term as a percentage.
	# 			percent = math.floor((tc.count * 100) / maximum)

	# 			# determine the CSS class for this term based on the percentage
	# 			if percent <= 20:
	# 				tc.css_class = 'tag-cloud-tiny'
	# 			elif 20 < percent <= 40:
	# 				tc.css_class = 'tag-cloud-small'
	# 			elif 40 < percent <= 60:
	# 				tc.css_class = 'tag-cloud-medium'
	# 			elif 60 < percent <= 80:
	# 				tc.css_class = 'tag-cloud-large'
	# 			else:
	# 				tc.css_class = 'tag-cloud-huge'
					
	# 			result.append(tc)

	# 	random.shuffle(result)
	# 	return result

	# Get date counts, sorted in reverse chronological order.
	def get_month_counts(self):
		hash = Article.get_all_datetimes()
		datetimes = hash.keys()
		date_count = {}
		for dt in datetimes:
			just_date = datetime.date(dt.year, dt.month, 1)
			try:
				date_count[just_date] += hash[dt]
			except KeyError:
				date_count[just_date] = hash[dt]

		dates = date_count.keys()
		dates.sort()
		dates.reverse()
		return [DateCount(date, date_count[date]) for date in dates]

	# Augment the ``Article`` objects in a list with the expanded
	# HTML, the path to the article, and the full URL of the article.
	# The augmented fields are:
	def augment_articles(self, articles, url_prefix, html=True):
		for article in articles:
			if html:
				try:
					article.html = article.body
				except AttributeError:
					article.html = ''
			article.path = '/%s' % article.key.id()
			article.url = url_prefix + article.path

	# Render a list of articles.
	def render_articles(self, articles, request, recent, 
						template_name='show-articles.html'):
		url_prefix = 'http://' + request.environ['SERVER_NAME']
		port = request.environ['SERVER_PORT']
		if port:
			url_prefix += ':%s' % port

		self.augment_articles(articles, url_prefix)
		self.augment_articles(recent, url_prefix, html=False)

		last_updated = datetime.datetime.now()
		if articles:
			last_updated = articles[0].published_when

		blog_url = url_prefix
		# tag_path = '/' + defs.TAG_URL_PATH
		# tag_url = url_prefix + tag_path
		date_path = '/' + defs.DATE_URL_PATH
		date_url = url_prefix + date_path
		media_path = '/' + defs.MEDIA_URL_PATH
		media_url = url_prefix + media_path

		template_variables = {'blog_name'    : defs.BLOG_NAME,
							  'blog_owner'   : defs.BLOG_OWNER,
							  'articles'     : articles,
							  # 'tag_list'     : self.get_tag_counts(),
							  'date_list'    : self.get_month_counts(),
							  'version'      : '0.3',
							  'last_updated' : last_updated,
							  'blog_path'    : '/blog',
							  'blog_url'     : blog_url,
							  'archive_path' : '/' + defs.ARCHIVE_URL_PATH,
							  # 'tag_path'     : tag_path,
							  # 'tag_url'      : tag_url,
							  'date_path'    : date_path,
							  'date_url'     : date_url,
							  'recent'       : recent}

		return self.render_template(template_name, template_variables)

	# Get up to ``defs.TOTAL_RECENT`` recent articles.
	def get_recent(self):
		articles = Article.published()

		total_recent = min(len(articles), defs.TOTAL_RECENT)
		if articles:
			recent = articles[0:total_recent]
		else:
			recent = []

		return recent

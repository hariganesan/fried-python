# Hari Ganesan 12/21/13
# taken from https://github.com/bmc/picoblog
# or http://brizzled.clapper.org/blog/2008/08/07/writing-blogging-software-for-google-app-engine/

import datetime
import sys

from google.appengine.ext import ndb

# If the local platform is 64 bit, just using sys.maxint can cause problems.
# It will evaluate to a number that's too large for GAE's 32-bit environment.
# So, force it to a 32-bit number.
# FETCH_THEM_ALL = ((sys.maxint - 1) >> 32) & 0xffffffff

####################
# Models and objects
####################


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
# class TagCount(object):
# 	def __init__(self, tag, count):
# 		self.css_class = ""
# 		self.count = count
# 		self.tag = tag


class Article(ndb.Model):
	title = ndb.StringProperty(required=True)
	body = ndb.TextProperty()
	published_when = ndb.DateTimeProperty(auto_now_add=True)
	# tags = ndb.StringProperty(repeated=True)
	# article_id = ndb.IntegerProperty()
	draft = ndb.BooleanProperty(required=True, default=False)

	# @classmethod
	# def get_all(cls):
	# 	# q = db.Query(Article)
	# 	# q.order('-published_when')
	# 	# return q.fetch(FETCH_THEM_ALL)
	# 	return Article.all()

	@classmethod
	def get(cls, article_id):
		# q = Article.all()
		# q.filter('id = ', id)
		# return q.get()
		return cls.get_by_id(article_id)

	@classmethod
	def published_query(cls):
		# q = Article.all()
		# q.filter('draft = ', False)
		# return q.get()
		return cls.query(Article.draft == False)

	@classmethod
	def published(cls):
		# q = Article.all()
		# q.filter('draft = ', False)
		# q.order('-published_when')
		# return q.fetch()
		return cls.query(Article.draft == False).order(-cls.published_when).fetch()

	# Return all tags, as TagCount objects, optionally sorted by frequency
	# (highest to lowest).
	# @classmethod
	# def get_all_tags(cls):
	# 	tag_counts = {}
	# 	for article in Article.published():
	# 		for tag in article.tags:
	# 			tag = unicode(tag)
	# 			try:
	# 				tag_counts[tag] += 1
	# 			except KeyError:
	# 				tag_counts[tag] = 1

	# 	return tag_counts

	@classmethod
	def get_all_datetimes(cls):
		dates = {}
		for article in Article.published():
			date = datetime.datetime(article.published_when.year,
									 article.published_when.month,
									 article.published_when.day)
			try:
				dates[date] += 1
			except KeyError:
				dates[date] = 1

		return dates

	@classmethod
	def all_for_month(cls, year, month):
		start_date = datetime.date(year, month, 1)
		if start_date.month == 12:
			next_year = start_date.year + 1
			next_month = 1
		else:
			next_year = start_date.year
			next_month = start_date.month + 1

		end_date = datetime.date(next_year, next_month, 1)
		return Article.published_query()\
					   .filter('published_when >=', start_date)\
					   .filter('published_when <', end_date)\
					   .order('-published_when')\
					   .fetch()

	# @classmethod
	# def all_for_tag(cls, tag):
	# 	return Article.published_query()\
	# 				  .filter('tags = ', tag)\
	# 				  .order('-published_when')\
	# 				  .fetch()

	# @classmethod
	# def convert_string_tags(cls, tags):
	# 	new_tags = []
	# 	for t in tags:
	# 		if type(t) == db.Category:
	# 			new_tags.append(t)
	# 		else:
	# 			new_tags.append(db.Category(unicode(t)))
	# 	return new_tags

	def __unicode__(self):
		return self.__str__()

	def __str__(self):
		return '[%s] %s' %\
			   (self.published_when.strftime('%Y/%m/%d %H:%M'), self.title)

	# def save(self, id):
	# 	previous_version = Article.get_by_id(id)
	# 	try:
	# 		draft = previous_version.draft
	# 	except AttributeError:
	# 		draft = False

	# 	if draft and (not self.draft):
	# 		# Going from draft to published. Update the timestamp.
	# 		self.published_when = datetime.datetime.now()

	# 	try:
	# 		obj_id = self.key().id()
	# 		resave = False
	# 	except ndb.NotSavedError:
	# 		# No key, hence no ID yet. This one hasn't been saved.
	# 		# We'll save it once without the ID field; this first
	# 		# save will cause GAE to assign it a key. Then, we can
	# 		# extract the ID, put it in our ID field, and resave
	# 		# the object.
	# 		resave = True

	# 	self.put()
	# 	if resave:
	# 		self.id = self.key().id()
	# 		self.put()

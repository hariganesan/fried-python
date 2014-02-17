# created by Hari Ganesan 2/14/14
# fried-python blog/admin handlers and routes

import os
import cgi
import logging

from models import *
import webapp2
import handlers

# Handles the main admin page, which lists all articles in the blog,
# with links to their corresponding edit pages.
class ShowArticlesHandler(handlers.BlogRequestHandler):
    def get(self):
        logging.info("ShowArticlesHandler invoked")
        articles = Article.get_all()
        template_vars = {'articles' : articles}
        self.response.out.write(self.render_template('admin-main.html',
                                                     template_vars))

# Handles requests to create and edit a new article.
class NewArticleHandler(handlers.BlogRequestHandler):
    def get(self):
        article = Article(title='New article',
                          body='Content goes here',
                          draft=True)
        template_vars = {'article' : article}
        self.response.out.write(self.render_template('admin-edit.html',
                                                     template_vars))

# Handles form submissions to save an edited article.
class SaveArticleHandler(handlers.BlogRequestHandler):
    def post(self):
        title = cgi.escape(self.request.get('title'))
        body = cgi.escape(self.request.get('content'))
        s_id = cgi.escape(self.request.get('id'))
        id = int(s_id) if s_id else None
        tags = cgi.escape(self.request.get('tags'))
        published_when = cgi.escape(self.request.get('published_when'))
        draft = cgi.escape(self.request.get('draft'))
        if tags:
            tags = [t.strip() for t in tags.split(',')]
        else:
            tags = []
        tags = Article.convert_string_tags(tags)

        if not draft:
            draft = False
        else:
            draft = (draft.lower() == 'on')

        article = Article.get(id) if id else None
        if article:
            # It's an edit of an existing item.
            just_published = article.draft and (not draft)
            article.title = title
            article.body = body
            article.tags = tags
            article.draft = draft
        else:
            # It's new.
            article = Article(title=title,
                              body=body,
                              tags=tags,
                              draft=draft)
            just_published = not draft

        article.save()

        if just_published:
            logging.debug('Article %d just went from draft to published.'
                           % article.id)
            # TODO: alert_the_media()

        edit_again = cgi.escape(self.request.get('edit_again'))
        edit_again = edit_again and (edit_again.lower() == 'true')
        if edit_again:
            self.redirect('/admin/article/edit/?id=%s' % article.id)
        else:
            self.redirect('/admin/')

# Handles requests to edit an article.
class EditArticleHandler(handlers.BlogRequestHandler):
    def get(self):
        id = int(self.request.get('id'))
        article = Article.get(id)
        if not article:
            raise ValueError, 'Article with ID %d does not exist.' % id

        article.tag_string = ', '.join(article.tags)
        template_vars = {'article'  : article}
        self.response.out.write(self.render_template('admin-edit.html',
                                                     template_vars))

# Handles form submissions to delete an article.
class DeleteArticleHandler(handlers.BlogRequestHandler):
    def get(self):
        id = int(self.request.get('id'))
        article = Article.get(id)
        if article:
            article.delete()

        self.redirect('/admin/')


logging.info("admin: os environ is " + os.environ['HTTP_HOST'])

# run the admin script
app = webapp2.WSGIApplication(
    [('/admin/?', ShowArticlesHandler),
     ('/admin/article/new/?', NewArticleHandler),
     ('/admin/article/delete/?', DeleteArticleHandler),
     ('/admin/article/save/?', SaveArticleHandler),
     ('/admin/article/edit/?', EditArticleHandler)
     ], debug=True)

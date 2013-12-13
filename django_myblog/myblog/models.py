from django.db import models
from django.contrib import admin
 
class Tag(models.Model):
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name

class Post(models.Model):
    title = models.CharField(max_length=64)
    post_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

myModels = [Tag, Post]
admin.site.register(myModels)
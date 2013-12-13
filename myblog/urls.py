from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'django_myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'page'),
	url(r'^blog/page(?P<num>\d+)/$', 'page'),
)
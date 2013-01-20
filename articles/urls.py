from django.conf.urls import patterns, include, url

urlpatterns = patterns('articles.views',
    url(r'^$', 'articles_all', name='articles_list'),
    url(r'^(?P<pk>\d+)/', 'article_details', name='article_details'),
    url(r'^(?P<slideshow_url>\w+)/(?P<pk>\d+)/', 'article_details'),
)


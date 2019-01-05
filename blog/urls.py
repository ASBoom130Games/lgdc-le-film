from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^google311f29b3ed4bd3be.html', views.google, name='google'),
	url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
	url(r'^Film$', views.film, name='film lgdc'),
	url(r'^Information$', views.info, name='info lgdc'),
	url(r'^description/(?P<pk>[0-9]+)/$', views.description_edit, name='description_edit'),
	#url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index')
]
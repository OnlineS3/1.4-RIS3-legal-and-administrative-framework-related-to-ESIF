from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='legaladmin_index'),
	url(r'^about$', views.about, name='legaladmin_about'),
	url(r'^guide$', views.guide, name='legaladmin_guide'),
	url(r'^related$', views.related, name='legaladmin_related'),
	url(r'^callback$', views.callback, name='legaladmin_callback'),
	url(r'^logoutview/$', views.logout, name='legaladmin_logoutview'),
	url(r'^access$', views.callback, name='legaladmin_access')
]
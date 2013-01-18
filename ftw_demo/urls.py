from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'ftw_demo.views.home', name='home'),
	# url(r'^ftw_demo/', include('ftw_demo.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^$', 'performance_groups.views.index'),
	url(r'^groups/$', 'performance_groups.views.index'),
	url(r'^groups/(?P<group_id>\d+)/$', 'performance_groups.views.detail'),
	url(r'^groups/(?P<group_id>\d+)/sub/$', 'performance_groups.views.subscribe'),
	url(r'^groups/(?P<group_id>\d+)/sub/subbed/$', 'performance_groups.views.subbed'),

	url(r'^bootstrap/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)

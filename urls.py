from django.conf.urls.defaults import *
import os

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),
    ('^posts/new/$', 'core.views.new_post'),
    ('^posts/$', 'core.views.list_posts'),
)
urlpatterns += patterns((''),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__),'static')}
    ),
)

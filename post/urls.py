'''
Urls module
'''

from django.conf.urls import url

from post.views import post as post_views
from post.views import comment as comment_views

urlpatterns = [  
    url(r'^$', post_views.HomeView.as_view(),
        name='index'),
    url(r'^new', post_views.PostView.as_view(),
        name='new'),
    url(r'^edit/(?P<id>\d+)/$', post_views.EditPostVIew.as_view(),
        name='edit'),
    url(r'^delete/(?P<id>\d+)/$', post_views.DeletePostView.as_view(),
        name='delete'),
    url(r'^list/(?P<id>\d+)/$', comment_views.CommentListView.as_view(),
        name='list'),
    
]
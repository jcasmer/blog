'''
Urls module
'''

from django.urls import path

from post.views import post as post_views
from post.views import comment as comment_views

app_name='post'

urlpatterns = [  
    path(r'', post_views.HomeView.as_view(),
        name='index'),
    path(r'new', post_views.PostView.as_view(),
        name='new'),
    path(r'edit/(?P<id>\d+)/$', post_views.EditPostVIew.as_view(),
        name='edit'),
    path(r'delete/(?P<id>\d+)/$', post_views.DeletePostView.as_view(),
        name='delete'),
    path(r'list/(?P<id>\d+)/$', comment_views.CommentListView.as_view(),
        name='list'),
    
]
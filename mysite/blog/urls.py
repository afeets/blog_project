from django.urls import path
from blog import views
from django.conf.urls import url

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    url(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    path(r'post/new/',views.CreatePostView.as_view(),name='post_new'),
    url(r'post/(?P<pk>\d+)/update$',views.UpdatePostView.as_view(),name='post_update'),
    url(r'post/(?P<pk>\d+)/delete$',views.DeletePostView.as_view(),name='post_delete'),
    path(r'drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'), # function based
    url(r'comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'), # function based
    url(r'comment/(?P<pk>\d+)/delete/$',views.comment_remove,name='comment_delete'), # function based
    url(r'post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'), # function based
    path('about',views.AboutView.as_view(),name='about'),
]

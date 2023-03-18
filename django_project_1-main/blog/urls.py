
from django.urls import path,include,re_path
from .views import post_views
from .views import comment_views
from django.contrib.auth.validators import UnicodeUsernameValidator
app_name = 'blog'

username_regex = UnicodeUsernameValidator.regex
urlpatterns=[


    path('',post_views.BlogList,name='post_list'),
    path('<int:post_pk>/',post_views.blog_detail ,name='post_detail'),
    path('create/',post_views.blog_create ,name='blog_create'),
    path('edit/<int:post_pk>/',post_views.blog_edit ,name='blog_edit'),
    path('delete/<int:post_pk>/',post_views.blog_delete ,name='blog_delete'),

    path('comment/create/<int:post_pk>',comment_views.comment_create,name='comment_create'),
    path('comment/edit/<int:comment_pk>',comment_views.comment_edit,name='comment_edit'),
    path('comment/delete/<int:comment_pk>',comment_views.comment_delete,name='comment_delete'),
    re_path(r'^(?P<username>[\w.@+-]+)/$',post_views.UserPage,name='user_page'),
]
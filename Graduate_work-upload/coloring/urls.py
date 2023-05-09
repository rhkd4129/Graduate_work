from django.urls import path,re_path
from . import views

app_name = 'coloring'

urlpatterns=[

     # path('',views.crawing,name = 'crawing'),
     path('',views.all,name = 'crawing'),
     path('upload/',views.upload_view,name = 'upload'),

     
     path('result/<int:advice_pk>/',views.crawing_result,name= 'result'),

     path('trans_image_result/<int:advice_pk>/<str:button_value>/',views.trans_image_result,name= 'trans_image_result'),
     re_path(r'^(?P<username>[\w.@+-]+)/$',views.user_page,name ='user_page'),

     # re_path(r'^(?P<username>[\w.@+-]+)/trans_image/(?P<keywords>[\w.@+-]+)/$', views.user_page_trans_image, name='user_page_trans_image'),
     re_path(r'^(?P<username>[\w.@+-]+)/trans_image/(?P<name>[\w.@+-]+)/(?P<keywords>[\w.@+-]+)/$', views.user_page_trans_image, name='user_page_trans_image'),
]    

  

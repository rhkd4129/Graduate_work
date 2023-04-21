from django.urls import path,re_path
from . import views

app_name = 'coloring'

urlpatterns=[

     path('',views.crawing,name = 'crawing'),
     path('result/<int:advice_pk>/',views.crawing_result,name= 'result'),
     path('trans_image_result/<int:advice_pk>/<str:button_value>/',views.trans_image_result,name= 'trans_image_result'),
     re_path(r'^(?P<username>[\w.@+-]+)/$',views.user_page,name ='user_page'),
     re_path(r'^(?P<username>[\w.@+-]+)/trans_image/$',views.user_page_trans_image,name ='user_page_trans_image'),
    #  path('download/<int:advice_pk>/<str:button_value>/',views.image_download, name = 'download'),
    #  path('search_image/',views.search_image, name = 'search_image'),

]
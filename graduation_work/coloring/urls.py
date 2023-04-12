from django.urls import path
from . import views



app_name = 'coloring'

urlpatterns=[

     path('',views.crawing,name = 'crawing'),
     path('result/<int:advice_pk>/',views.crawing_result,name= 'result'),
     path('trans_image_result/<int:advice_pk>/<str:button_value>/',views.trans_image_result,name= 'trans_image_result'),
    #  path('download/',views.file_download, name = 'download'),
    #  path('search_image/',views.search_image, name = 'search_image'),
    # path(),
]
from django.urls import path
from . import views



app_name = 'qwer'

urlpatterns=[

     path('',views.qwer,name = 'qwer'),
     path('result/<int:advice_pk>/',views.result,name= 'result')
    #  path('search_image/',views.search_image, name = 'search_image'),
    # path(),
]
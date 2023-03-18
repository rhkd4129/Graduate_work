from django.urls import path
from . import views
app_name = 'crawling'

urlpatterns=[

     path('',views.melon_chart,name = 'melon_chart'),
    # path(),
]
from django.urls import path
from . import views
app_name = 'crawling'

urlpatterns=[

     path('melon_chart/',views.melon_chart,name = 'melon_chart'),
     path('search_image/',views.search_image, name = 'search_image'),
    # path(),
]
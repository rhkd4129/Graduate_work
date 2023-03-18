from django.urls import path
from django.views.generic import TemplateView


app_name = 'eng'
urlpatterns=[

    path('',TemplateView.as_view(Templatename= 'eng/home.html'),name='home'),




]
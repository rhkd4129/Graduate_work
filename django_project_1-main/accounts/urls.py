from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name ='accounts'

urlpatterns=[
    path('login/',LoginView.as_view(template_name = 'accounts/login.html'),name = 'login'),
    path('signup/',views.signup,name ='signup'),
    path('logout/',LogoutView.as_view(template_name = 'accounts/logout.html'),name ='logout'),
    path('edit/',views.profile_edit,name ='profile_edit'),
    path('password_change/',views.password_change,name ='password_change'),
    




]
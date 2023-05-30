from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import TView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TView.as_view(),name ='home'),
    path('accounts/',include('accounts.urls')),
    path('coloring/',include('coloring.urls')),

]

if settings.DEBUG:#미디어파일에 대한 스태틱 서브기능?
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


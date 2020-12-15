from django.contrib import admin
from django.urls import path, include
from solicitudes import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),    
]

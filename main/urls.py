"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import settings
from django.conf.urls.static import static

from .views import * #to import all function default otherwise we use : from .views import index,loginPage,registerPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("login",loginPage),
    path("register",registerPage),
    path("registerUser",registerUser),
    path("loginUser",loginUser)
]

# To acess photos from local device and also change in setting
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
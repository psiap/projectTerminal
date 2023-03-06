"""drfsitewc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from wcapi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/statistics', WcapiAPIViewStatistics.as_view()),
    path('api/v1/history', WcapiAPIViewHistory.as_view()),
    path('api/v1/settings', WcapiAPIViewSettings.as_view()),
    path('api/v1/qr', WcapiAPIViewQR.as_view()),
    path('api/v1/login', WcapiAPIViewCheckLogin.as_view()),
    path('api/v1/auth', WcapiAPIViewCheckAuth.as_view()),
    path('api/v1/checkorder',WcapiAPIViewCheckOrder.as_view()),
    path('api/v1/convectorvalut',WcapiAPIViewConvectorValut.as_view())
]

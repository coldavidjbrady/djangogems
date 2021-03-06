"""djangogems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^store/', include('store.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from store.urls import router
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/token/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'api-token-refresh/', refresh_jwt_token),
]

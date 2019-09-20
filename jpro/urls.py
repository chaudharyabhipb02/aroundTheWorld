"""jpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls import url
urlpatterns=[
    url(r'^abhi/',include('abhi.urls')),
    url(r'^admin/',admin.site.urls),
    url(r'^arsh/',include('abhi.urls')),
    url(r'^baba/',include('abhi.urls')),
    url(r'^myapp/',include('abhi2.urls')),
    url(r'^app/',include('abhi3.urls')),
    url(r'^pro/',include('myapp.urls'))
            ]
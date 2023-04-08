"""shopify_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

admin.site.site_header = "Aravenda Shopify Metafields"
admin.site.site_title = "Aravenda Shopify Metafields"
admin.site.index_title = "Welcome to Aravenda Shopify Metafields"
admin.site.enable_nav_sidebar = False  # added 27/1/21 kc to deal with weird side bar issue


urlpatterns = [
    path('shopify/', include('shopify_app.urls')),
    path('', include('home.urls')),
]









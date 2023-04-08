
print("!!!!!!!!!!!!!!!!!!!!! loading  home/urls.py")

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='root_path'),
]

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.phone_comment),
    re_path(r'^/search', views.search),
]

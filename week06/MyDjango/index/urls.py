from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.movie_comment),

    ### 增加一个输出电影评论的路径
    path('comment', views.movie_comment),

    path('search/', views.search),
]
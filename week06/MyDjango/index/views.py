# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import register_converter

from . import converters
from .models import comment

def myyear(request, year):
    return render(request, 'yearview.html')

# 输出电影评论的数据到模板上面
def movie_comment(request):
    #condtions = {'stars__gt': 3}
    n = comment.objects.filter(stars__gt=3).all()
    #comments = n.comment_text[0]
    return render(request, 'index.html', locals())



# 输出查询按钮的数据到模板上面
def search(request):
    q = request.GET.get('q')
    print(q)
    error_msg = ''

    if not q or q =='':
         error_msg = '请输入关键词'
         return render(request, 'errors.html', {'error_msg': error_msg})
    n = comment.objects.filter(comment_text__icontains=q)
    return render(request, 'index.html',locals())
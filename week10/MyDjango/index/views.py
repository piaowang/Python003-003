# Create your views here.
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import register_converter
from django.views.decorators.csrf import csrf_exempt

from .form import LoginForm
from django.contrib.auth import authenticate, login
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

@csrf_exempt
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            if len(cd['password'])<2:
                raise ValidationError('Password too short')

            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                #login(request, user)
                return render(request, 'result2.html', locals())
                #HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form.html', {'form': login_form})
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import T1
from django.db.models import Avg

def phone_comment(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {T1.objects.aggregate(Avg('rank'))['rank__avg']:0.1f} "

    # 情感倾向
    sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    #return render(request, 'douban.html', locals())
    return render(request, 'phone/result.html', locals())

# 输出查询按钮的数据到模板上面.
@csrf_exempt
def search(request):
    q = request.GET.get('phone_search')
    print(1)
    print(list(request.GET))
    print(q)
    error_msg = ''
    if not q or q =='':
         error_msg = '请输入关键词000'
         return render(request, 'errors.html', {'error_msg': error_msg})
    n = T1.objects.filter(commnet_text__icontains=q)

    shorts = n.all()
    # 评论数量
    counter = n.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {n.aggregate(Avg('rank'))['rank__avg']:0.1f} "

    # 情感倾向
    sent_avg =f" {n.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = n.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = n.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    return render(request, 'phone/result.html',locals())
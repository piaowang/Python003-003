from django.contrib import admin

# Register your models here.
from .models import Type, Name,comment
# 注册模型
admin.site.register(Type)
admin.site.register(Name)
admin.site.register(comment)
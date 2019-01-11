from django.shortcuts import render, render, redirect
from django.http import HttpResponse
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from .models import *
import json
# 打印日志
import logging


# Create your views here.

# 注册功能
def register(requests):
    # 判断请求是post/get
    # 拿到前端的数据
    # 判断有没有该用户
    # 有: 登录>>>
    # 没有: 注册信息
    # 返回数据找到相应的页面
    if requests.menthod == 'POST':
        new_user = UserInfo()
        new_user.username = requests.POST.get('username')
        try:
            olduser = UserInfo.objects.filter(username=new_user.username)
            if len(olduser) > 0:
                return render(requests, 'register.html', {'message': '用户名已存在'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if requests.PSOT.get('pwd') != requests.POST.get('cpwd'):
            return render(requests, 'register.html', {'message': '两次密码不一致'})
        new_user.password = make_password(requests.POST.get('pwd'), None, 'pbkdf2_sha1')
        # check_password()
        new_user.save()
        return render(requests, 'login.html')


def login_(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('pwd')
        # 用户名密码为空
        # django自带的一套验证,封装好的方法, 可以直接验证数据库里面的数据是否相等
        # 如果有的话,得到的user是一个对象.没有的话则是空
        user = authenticate(username=uname, password=pwd)
        if user is not None and user.is_active:
            # django自带的登录系统
            login(request, user)
            url = request.COOKIES.get('source_url', '')
            return render(request, 'index.html')


def logout_(request):
    logout(request)
    return render(request, 'index.html')

# def register_(request):
    # 验证用户是否具有合法性,也就是说用户是否可以登录进去
    # 作用和装饰器的用法是类似的,判断用户名是否已经登录的
    # if request.user.is_authenticated():

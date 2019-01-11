"""usedcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
# 扩展内容
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^buy/', include('buy.urls')),
    url(r'^front/', include('front.urls')),
    url(r'^pay/', include('pay.urls')),
    url(r'^userinfo/', include('userinfo.urls')),
    url(r'^sale/', include('sale.urls')),
    # 直接跳转到某个模板,不进行后端操作
    # url(r'^a/',TemplateView.as_view(template_name='upimg.html'),name='index')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

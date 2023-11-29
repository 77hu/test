"""
URL configuration for mysql_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mysql_te import views

from django.urls import re_path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('te_test1/', views.te_test1),
    # path('mysql_te/', include("mysql_te.urls"))
    # 正则化表达式[0-9]表示取值范围，{4}表示重复匹配的数值个数，{1，2}这里表示取1或2位数，$结束符
    re_path(r'^(?P<date>[0-9]{4}/[0-9]{1,2}/[0-9]{1,2})/$', views.date_view)
]

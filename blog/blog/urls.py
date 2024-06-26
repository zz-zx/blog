"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()



from django.contrib import admin
from django.urls import path,include

#1.导入系统的 logging
import logging
# #创建（获取）日志器
# logger=logging.getLogger('django')
#
# from django.http import HttpResponse
# def log(request):
#     # 3.使用日志器记录信息
#     logger.info('info')
#     return HttpResponse('test')



urlpatterns = [
    path('admin/', admin.site.urls),
    #include 的参数中设计一个元组
    path('',include(('users.urls', 'users'), namespace='users'))
   # path('',log),
]

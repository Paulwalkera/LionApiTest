"""dev07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

# from projects.views import index, get_project
from projects import views

# 一、什么是路由？
# 1.定义
#    指url与后端视图之间的一一映射关系

# 2.添加
#   1）需要在全局路由文件（urls.py），urlpatterns列表中添加路由条目
#   2）urlpatterns列表条目总数就是路由总数
#   3）urlpatterns列表从上到下进行匹配（路由寻址）
#   4）urlpatterns列表中条目一旦匹配成功，就会终止往下匹配
#   5）urlpatterns列表中条目匹配不成功，就会一直往下匹配
#   6）如果全部条目都匹配不成功，那么会抛出404异常（404页面）

# 3.path函数
#   1）用于定义路由条目
#   2）第一个参数为url路径参数（字符串），路径最前面不添加/，路径最后面需要添加/
#   3）第二个参数为视图函数或者类视图，如果添加的视图函数，无需使用()调用
#   4）如果第二个参数为include，那么会继续进入到子路由中匹配，子路由的匹配规则与全局路由匹配规则一致
#   5）第一个参数可以使用类型转化器
#       <类型转化器:参数名称>
#       默认的类型转化器：int、str、slug、uuid
#       参数名称，在调用视图时，会自动传递给视图函数，需要使用同名的参数接收

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Lemon API接口文档平台",  # 必传
        default_version='v1',  # 必传
        description="这是一个美轮美奂的接口文档",
        terms_of_service="http://api.keyou.site",
        contact=openapi.Contact(email="keyou100@qq.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', include('projects.urls')),
    path('', include('interfaces.urls')),
    path('', include('reports.urls')),
    path('', include('envs.urls')),
    path('', include('debugtalks.urls')),
    path('', include('testsuites.urls')),
    path('', include('testcases.urls')),
    path('', include('configures.urls')),
    path('', include('testsuites.urls')),
    path('', include('summary.urls')),

    path('docs/', include_docs_urls(title='测试平台接口文档', description='xxx接口文档')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/', include('rest_framework.urls')),
    path('user/', include('users.urls')),
]

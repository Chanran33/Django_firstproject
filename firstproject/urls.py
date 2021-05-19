"""firstproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from firstapp import views as first#view.py를 urls.py에서 이용할 수 있도록 import해줘야함
from wordCount import views as wc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first.welcome,name="welcome"), #아무것도 안적힌 주소는 처음 시작시 나오는 페이지를 뜻함 
    #다른 html파일에서 welcome url을 입력하는 것 대신에 쓸 수 있는 이름을 적어준다.(url대신 사용할 수 있음)
    path('hello/',first.hello,name="hello"),
    path('wc/',wc.home,name="wc"),
    path('wc/result/', wc.result, name="result"),
]

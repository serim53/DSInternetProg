"""myInternetPrj URL Configuration

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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# urls.py
# 표지판 역할
# 장고로 개발한 웹 사이트에 방문했을 때 어떤 페이지로 들어가야 하는지 알려줌
# import로 path랑 include 해줘야함
# path(서버IP/작성된 주소, 호출될 함수)

urlpatterns = [
    # 기본적으로 처음에는 blog앱에 urls파일이 없지만, 추후 추가할 것임
    # 따라서 먼저 path에 blog.urls 파일을 include함을 작성해주어야 함
    # 프로젝트쪽에서 blog라는 url로 들어갔을 때 blog라는 앱에서 처리하도록 처리
    # blog 아래에 urls.py 파일 추가해줄 것
    path('blog/', include('blog.urls')), # 서버IP/blog
    path('admin/', admin.site.urls),    # 서버IP/admin
    path('', include('single_pages.urls')), # 서버IP/
    path('accounts/', include('allauth.urls')),
    path('markdownx/', include('markdownx.urls'))
    # single_pages 아래에 urls.py 추가해줄 것
]

# url : IP주소/media
# 저장 폴더 : 프로젝트 BASE_DIR/_media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 서버IP/media
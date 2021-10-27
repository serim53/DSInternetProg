from django.urls import path
from . import views

urlpatterns = [ # 서버IP/
    # 대문페이지
    path('', views.landing), # 서버IP/
    # views에서 함수 생성해줄 것
    # about_me 페이지
    path('about_me/', views.about_me) # 서버IP/about_me/

]
from django.urls import path

from . import views

urlpatterns = [ # 서버IP/blog
#    path('<int:pk>/', views.single_post_page),
#    path('', views.index),

    path('category/<str:slug>', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    # '' 빈칸으로 보이지만, 현재 위치를 의미하므로 서버 IP/blog를 의미함
    # blog/라는 url이 설정되었을 때 views에 있는 함수가 실행되는데
    # 기본적으로 views에 아무것도 작성되어 있지 않으므로 작성을 하러 이동해야 함

]
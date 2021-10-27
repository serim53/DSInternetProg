from django.db import models
from django.contrib.auth.models import User
import os

# 수정 다 될때마다 마이그레이션 시켜줄 것!!

# 모델에 대한 정보를 정의하고 저장하는 파일.
# 테이블을 생성하고 테이블의 필드가 정의된 파일

# 데이터베이스를 만들고 migration을 해줘야 함

# python manage.py makemigrations
# No changes detected가 나오면 장고 프로젝트의 settings.py의
# INSTALLED_APPS에 앱을 추가해주어야 함
# 이 프로젝트에서는 'blog', 'single_pages'를 추가해 주었음
# 이후 다시 makemigrations
# 그 다음 포스트 모델을 데이터베이스에 반영하기 위해
# python manage.py migrate
# Post라는 모델을 admin 페이지에서 나타나게 하기 위해
# blog/admin.py에서 admin.site.register(Post) 을 작성해준다.

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text= models.CharField(max_length=100, blank=True)
    content = models.TextField()
    # 이미지 저장 위치 지정
    # blank='true'로 지정했으므로 데이터가 없는 것도 가능하다
    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%y/%m/%d/', blank=True)
    # 시간에 대한 설정은 원래 프로젝트폴더 myInternetProject의
    # settings.py의 TIME_ZONE 값을 'Asia/Seoul'로 바꿔준다
    # auto_now_add=True 속성은 자동으로 날짜가 생성되어서 추가되는 속성
    # settings.py의 USE_TZ = False로 바꿔줄 것!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #author
    # CASCADE : USER에서 어떠한 사용자의 계정이 사라지면 그의 포스트도 다 사라짐
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author을 null로 처리하고, delete되었을때도 null로 처리 가능
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # 목록에 보여질 제목을 설정 , pk는 아이디값
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    # 파일 이름 가져옴 (post_detail에서 사용)
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    # 파일 확장자 가져옴
    # "abc.txt".split('.') = {"abc", "txt"}
    # [-1]은 가장 마지막 원소를 의미
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

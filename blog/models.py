from django.db import models
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text= models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #author

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    # 파일 이름 가져옴
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    # 파일 확장자 가져옴
    # "abc.txt".split('.') = {"abc", "txt"}
    # [-1]은 가장 마지막 원소를 의미
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

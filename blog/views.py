from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PostList(ListView) :
    model = Post
    ordering = '-pk'
#    template_name = 'blog/post_list.html'
# post_list.html

class PostDetail(DetailView) :
    model = Post
# post_detail.html

# def index(request) :
#     # pk를 기준으로 정렬을 하고 거꾸로 해주기 위해 앞에 -를 붙여줌
#     # 이렇게 해야 글이 최신순으로 보여짐
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/post_list.html',
#                   {
#                       'posts' : posts
#                   }
#                   )

# def single_post_page(request, pk) :
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html',
#                   {
#                       'post': post
#                   }
#                   )
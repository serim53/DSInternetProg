from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category


# Create your views here.

class PostList(ListView) :
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

#    template_name = 'blog/post_list.html' # 부를 파일을 직접 지정하고 싶은 경우
# post_list.html이 불려지는 것

class PostDetail(DetailView) :
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# post_detail.html이 불려지는 것

def category_page(request, slug):
    if slug == 'no_category' :
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(request, 'blog/post_list.html',
                  {
                      'post_list' : post_list,
                      'categories' : Category.objects.all(),
                      'no_category_post_count' : Post.objects.filter(category=None).count(),
                      'category' : category
                  }
                  )

# (2)
# def index(request) :
#     # pk를 기준으로 정렬을 하고 거꾸로 해주기 위해 앞에 -를 붙여줌
#     # 이렇게 해야 글이 최신순으로 보여짐
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/post_list.html',
#                   {
#                       'posts' : posts
#                   }
#                   )

# (1)
# 렌더링 / render(request, 그려진 템플릿(출력할 문서))
# view에서 보여지는 구조와 실제 파일 위치와 다름
# blog/post_detail.html은 실제로는 blog/templates/blog/post_detail.html
# 경로임

# def single_post_page(request, pk) :
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html',
#                   {
#                       'post': post
#                   }
#                   )
from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# 테스트 주도 개발을 위한 파일
# python manage.py test

# pip install beautifulsoup4
# 브라우저에 구현한 내용이 제대로 표현되었는지 확인하기 위한 라이브러리

# Create your tests here.
class TestView(TestCase):

    # setUp함수는 테스트 실행 전에 공통적으로 수행할 작업의 내용을 넣어줌
    def setUp(self):
        self.client = Client()

    def navbar_test(self, soup):
        # 네비게이션바가 있다
        navbar = soup.nav
        # 네비게이션바에 Blog, AboutMe라는 문구가 있는지 확인
        # assertIn(a,b) : a in b
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        logo = navbar.find('a', text='InternetProgramming')
        self.assertEqual(logo.attrs['href'], '/')
        home = navbar.find('a', text='Home')
        self.assertEqual(home.attrs['href'], '/')
        blog = navbar.find('a', text='Blog')
        self.assertEqual(blog.attrs['href'], '/blog')
        about = navbar.find('a', text='About Me')
        self.assertEqual(about.attrs['href'], '/about_me')

    # post_list에 대한 테스트 코드!
    def test_post_list(self):
        # 포스트 목록 페이지를 가져온다
        # blog/라는 주소를 통해 목록 페이지를 가져와서 결과를 response에 저장
        response = self.client.get('/blog/')
        # 정상적으로 페이지가 로드
        # status_code를 통해 응답 상태를 확인. 200은 OK라는 상태
        self.assertEqual(response.status_code,200)
        # 페이지 타이틀 'Blog'
        # response.content를 html.parser를 통해 분석하고 그 결과를 soup에 저장
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')

        self.navbar_test(soup)
        # # 네비게이션바가 있다
        # navbar = soup.nav
        # # 네비게이션바에 Blog, AboutMe라는 문구가 있는지 확인
        # # assertIn(a,b) : a in b
        # self.assertIn('Blog', navbar.text)
        # self.assertIn('About Me', navbar.text)

        # 포스트(게시물)이 하나도 없는 경우
        self.assertEqual(Post.objects.count(), 0)
        # 적절한 안내 문구가 포함되어 있는지
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        # 포스트(게시물)이 2개 존재하는 경우
        # 임의의 2개의 게시물을 만들었음
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World!!! We are the world...'
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트입니다.',
            content='1등이 전부가 아니잖아요'
        )
        self.assertEqual(Post.objects.count(), 2)
        # 목록페이지를 새롭게 불러와서
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 포스트(게시물)의 타이틀이 2개 존재
        main_area = soup.find('div', id='main-area')
        # 테스트했을 때 NoneType object has no attribute 'text'는
        # main_area가 없다는 뜻임
        # 따라서, post_list에 가서 <div>태그에서 적절한 값을 넣어주어야 함
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

    # post_detail에 대한 테스트 코드!
    def test_post_detail(self):
        # 포스트 하나
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World!!! We are the world...'
        )
        # 이 포스트의 url이 /blog/1
        self.assertEqual(post_001.get_absolute_url(), '/blog/1')
        # url에 의해 정상적으로 상세페이지를 불러오는가
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code,200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.navbar_test(soup)
        # # 포스트목록과 같은 네비게이션바가 있는가
        # navbar = soup.nav
        # self.assertIn('Blog', navbar.text)
        # self.assertIn('About Me', navbar.text)
        # 포스트의 title은 웹브라우저의 title에 있는가
        self.assertIn(post_001.title, soup.title.text)
        # 포스트의 title은 포스트영역에도 있는가
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id="post-area")
        self.assertIn(post_001.title,post_area.text)
        # 포스트 작성자가 있는가
        # 아직 작성중
        # 포스트의 내용이 있는가
        self.assertIn(post_001.content, post_area.text)
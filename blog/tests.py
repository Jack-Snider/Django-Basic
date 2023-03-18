from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.

class TestView( TestCase ):

    def setUp(self):
        self.client = Client() # 웹사이트를 방문하는 사람의 브라우저 정보

    # 보통 TestCase를 상속받으면 그 안의 함수들은 함수이름 앞에 test가 있으면 하나의 unit test로 인식을 한다.
    # 근데 이건 그냥 함수로만 사용하고자 할 때는 이름앞에 test를 붙히지 않는다.
    def navbar_test( self, soup ):

        # 1.4 NavBar가 있다.
        navbar = soup.nav  # navbar라는 변수에 html코드로 가져온 soup변수에 있는 nav태그 저장

        # 1.5 Blog, About me라는 문구가 Navbar에 있다.
        self.assertIn('Blog', navbar.text)  # 'Blog'라는 문구가 soup의 nav태그의 텍스트로 있어야 한다. ( soup.nav.text로도 가능 ), 이미 navbar변수를 만들었기 때문에 navbar사용할게 그냥
        self.assertIn('About me', navbar.text)  # 'About me'라는 문구가 soup의 nav태그의 텍스트로 있어야 한다.

        logo_btn = navbar.find( 'a', text = 'Jack Snider' )
        self.assertEqual( logo_btn.attrs[ 'href' ], '/' ) # logo_btn태그의 속성중에 href이라는 속성이 '/'인걸 찾는다.

        home_btn = navbar.find( 'a', text = 'Home' )
        self.assertEqual( home_btn.attrs[ 'href' ], '/' )

        blog_btn = navbar.find('a', text='Blog')
        self.assertEqual( blog_btn.attrs[ 'href' ], '/blog/' )

        about_me_btn = navbar.find('a', text='About me')
        self.assertEqual( about_me_btn.attrs[ 'href' ], '/about_me/' )

    def test_post_list( self ):

        # 1.1 포스트 목록 페이지( post list )를 연다
        response = self.client.get( '/blog/' ) # 방문자의 브라우저에서 해당 url을 요청

        # 1.2 정상적으로 페이지가 로드된다.
        self.assertEqual( response.status_code, 200 ) # 요청 결과가 200인가? 반환값 : Bool

        # 1.3 페이지의 타이틀의 Blog라는 문구가 있다.
        soup = BeautifulSoup( response.content, "html.parser" ) # 요청한 결과의 내용물을 가져오는데 그건 html형태이다.
        self.assertIn( 'Blog', soup.title.text ) # 'Blog'라는 문구가 soup의 title태그의 text에 있어야 한다.

        self.navbar_test( soup )

        # 2.1 게시물이 하나도 없을 때
        self.assertEqual( Post.objects.count(), 0 ) # Post객체가 0개일 때

        # 2.2 메인 영역에 "아직 게시물이 없습니다" 문구가 나온다.
        main_area = soup.find( 'div', id = 'main-area' ) # div태그를 찾는데 id가 'main-area'인 것을 찾는다.
        self.assertIn( '아직 게시물이 없습니다', main_area.text ) # main_area라고 만든 변수의 text내용 중에 '아직 게시물이 없습니다' 문구가 있는지 확인

        # 3.1 만약 게시물이 2개 있다면,
        post_001 = Post.objects.create(
            title = '첫번째 포스트 입니다.',
            content = 'Hello, World. We are the World.',
        )

        post_002 = Post.objects.create(
            title='두번째 포스트 입니다.',
            content='저는 쌀국수를 좋아합니다.',
        )

        self.assertEqual( Post.objects.count(), 2 )

        # 3.2 포스트 목록 페이지를 새로 고침했을 때,
        response = self.client.get( '/blog/' )
        soup = BeautifulSoup( response.content, 'html.parser' )

        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다.
        main_area = soup.find( 'div', id = 'main-area' )
        self.assertIn( post_001.title, main_area.text ) # post_001의 title이 main_area에 text에 있어야 한다.
        self.assertIn( post_002.title, main_area.text )

        # 3.4 "아직 게시물이 없습니다" 라는 문구가 없어야 한다.
        self.assertNotIn( '아직 게시물이 없습니다', main_area.text ) # '아직 게시물이 없습니다'라는 문구는 main_area의 text에 없어야한다.

    def test_post_detail( self ):

        # 1.1 포스트가 하나 있다.
        post_001 = Post.objects.create(
            title='첫번째 포스트 입니다.',
            content='Hello, World. We are the World.',
        )
        self.assertEqual( Post.objects.count(), 1 )

        # 1.2 그 포스트의 url은 '/blog/1/'이다.
        self.assertEqual( post_001.get_absolute_url(), '/blog/1/' )

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1 첫 번째 포스트의 url로 접근하면 정상적으로 response가 온다( status code : 200 )
        response = self.client.get( post_001.get_absolute_url() )
        self.assertEqual( response.status_code, 200 )  # 요청 결과가 200인가? 반환값 : Bool

        soup = BeautifulSoup( response.content, 'html.parser' )

        self.navbar_test(soup)

        # 2.3 첫 번째 포스트의 제목이 웹 브라우저 탭 타이틀에 들어 있다.
        self.assertIn( post_001.title, soup.title.text ) # post_001의 title이 soup.title에 있어야 한다.

        # 2.4 첫 번째 포스트의 제목이 포스트 영역에 있다.
        main_area = soup.find( 'div', id = 'main-area' )
        post_area = main_area.find( 'div', id = 'post-area' )
        self.assertIn( post_001.title, post_area.text )

        # 2.5 첫 번째 포스트으 작성자( author )가 포스트 영역에 있다( 아직 구현할 수 없음 )

        # 2.6 첫 번째 포스트의 내용( content )이 포스트 영역에 있다.
        self.assertIn(post_001.content, post_area.text)


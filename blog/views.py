from django.shortcuts import render
from .models import Post

from django.views.generic import ListView # 장고에서 제공하는 목록을 보여주는 기능

# Create your views here.

class PostList( ListView ):
    model = Post
    #template_name = 'blog/index.html' # 템플릿을 지정해줌 ( 장고에서 제공 )
    # 사실  html파일을 post_html과 같이 변경하면 template_name도 필요없음
    ordering = '-pk'

# def index( request ):
#
#     '''
#     order_by( 'pk' ) : pk순서대로
#     order_by( '-pk' ) : pk의 역순대로
#     '''
#     posts = Post.objects.all().order_by( '-pk' )
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

def single_post_page( request, pk ):

    post = Post.objects.get( pk = pk ) # Post객체중에 pk가 파라미터로 받은 pk인 객체를 가져와라.

    return render(
        request,
        'blog/single_page.html',
        {
            'post':post,
        }
    )
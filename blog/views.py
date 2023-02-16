from django.shortcuts import render
from .models import Post

# Create your views here.

def index( request ):

    '''
    order_by( 'pk' ) : pk순서대로
    order_by( '-pk' ) : pk의 역순대로  
    '''
    posts = Post.objects.all().order_by( '-pk' )

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page( request, pk ):

    post = Post.objects.get( pk = pk ) # Post객체중에 pk가 파라미터로 받은 pk인 객체를 가져와라.

    return render(
        request,
        'blog/single_page.html',
        {
            'post':post,
        }
    )
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
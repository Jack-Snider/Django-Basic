from django.urls import path
from . import views # 해당 폴더에서 views를 가져와라

urlpatterns = [

    path( '<int:pk>/' , views.single_post_page ), # 정수형 파라미터를 받는데 변수 이름은 pk
    path( '', views.PostList.as_view() ), # views 파일에 있는 PostList 클래스를 뷰로 사용하겠다. ( as_view()는 약속이라고 생각하셈 일단 )


]
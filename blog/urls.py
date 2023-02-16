from django.urls import path
from . import views # 해당 폴더에서 views를 가져와라

urlpatterns = [

    path( '<int:pk>/' , views.single_post_page ), # 정수형 파라미터를 받는데 변수 이름은 pk
    path( '', views.index ), # 만약 blog 이후에 아무 url도 없다면 views파일에 index를 실행


]
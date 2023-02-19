from django.urls import path
from . import views # 해당 폴더에서 views를 가져와라

urlpatterns = [

    path( 'about_me/', views.about_me ),
    path( '', views.landing ), # 만약 single_pages 이후에 아무 url도 없다면 views파일에 landing 함수를 실행


]
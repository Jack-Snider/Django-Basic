from django.urls import path
from . import views # 해당 폴더에서 views를 가져와라

urlpatterns = [

    path( '', views.index ), # 만약 blog 이후에 아무 url도 없다면 views파일에 index를 실행

]
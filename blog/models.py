from django.db import models
import os
from django.contrib.auth.models import User # 사용자 계정을 위한 장고 라이브러리

# Create your models here.

# You can consider Object( Which is made by Class )
# can be one table in database
# like Class == Table name (  also can be Object )
# fields == Attribute ( Like in Database )
# Object -> Post .. .. ( Can be other class also )
# Django에서 models.py에 있는 각각의 클래스는 장고에서 제공하는 DB에 테이블로 들어간다. ( 클래스 이름 : 테이블 이름, 클래스 안에 있는 필드 : 속성 ) → 클래스로 찍어낸 하나의 객체가 DB로 치면 하나의 튜플
class Post( models.Model ):
    title = models.CharField(max_length=50)  # 게시물의 제목 , 최대 글자 50자
    hook_text = models.CharField(max_length=100, blank=True)  # 블로그 내용 요약을 위한 char필드
    content = models.TextField()  # 게시물의 내용

    '''
        auto_now_add : 새로 만들어졌을 때 현재시간을 자동으로 반영
        auto_now : 수정 되었을 때 자동으로 현재시간을 반영
    '''
    # blog/images/년/월/일 폴더에 저장 ( _media/blog/images/년/월/일/ 폴더에 저장, blank는 파일이 있어도, 없어도 된다.
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)  # file을 업로드 하기 위한 필드

    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    # 사용자
    # User객체가 삭제될 경우 그 객체를 외래키로 참고하고 있는 테이블의 튜플도 함께 삭제
    # on_delete = models.CASCADE → 해당 유저가 삭제됬을 때 그 유저와 관련된 모든 데이터도 삭제( 예 : 게시글 )
    # on_delete = models.SET_NULL → 해당 유저가 삭제되도 그 유저와 관련된 데이터의 주인이 None으로 바뀐다. ( 즉, 게시글과 같은 데이터의 소유자가 None으로 변경이 됨 [ 게시글 작성자에 대하여 삭제된 작성자라면 None으로 표시하게 된다. ] )
    # null = True → null을 허용하는 옵션
    author = models.ForeignKey( User, null=True ,on_delete = models.SET_NULL )



    def __str__(self):
        # 따로 pk값을 설정하지 않았지만 장고에서 Object가 생성되면 pk를 자동으로 생성해준다.
        return f'[{self.pk}] {self.title} :: {self.author}'

    # 각 객체의 고유의 url을 만들기 위한 함수
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # 장고에서 제공하지 않는 개발자가 직접 만든 함수
    def get_file_name(self):
        # 객체의 파일명을 가져옴
        return os.path.basename(self.file_upload.name)

    # 장고에서 제공하지 않는 개발자가 직접 만든 함수
    def get_file_ext(self):
        # 객체의 파일명을 가져와 확장자를 리턴
        return self.get_file_name().split('.')[-1]

from django.db import models
import os
# Create your models here.
class Post( models.Model ):
    
    title = models.CharField( max_length = 50 ) # 게시물의 제목 , 최대 글자 50자
    content = models.TextField() # 게시물의 내용

    '''
        auto_now_add : 새로 만들어졌을 때 현재시간을 자동으로 반영
        auto_now : 수정 되었을 때 자동으로 현재시간을 반영
    '''
    # blog/images/년/월/일 폴더에 저장 ( _media/blog/images/년/월/일/ 폴더에 저장, blank는 파일이 있어도, 없어도 된다.
    head_image = models.ImageField( upload_to='blog/images/%Y/%m/%d/', blank=True )
    file_upload = models.FileField( upload_to='blog/files/%Y/%m/%d', blank=True ) # file을 업로드 하기 위한 필드

    created_at = models.DateTimeField( auto_now_add = True ) # 작성 시간
    updated_at = models.DateTimeField( auto_now = True ) # 수정 시간  
    #author : 추후 작성

    def __str__( self ):

        # 따로 pk값을 설정하지 않았지만 장고에서 Object가 생성되면 pk를 자동으로 생성해준다.
        return f'[{self.pk}] {self.title}'

    # 각 객체의 고유의 url을 만들기 위한 함수
    def get_absolute_url( self ):
        return f'/blog/{ self.pk }/'
    
    # 장고에서 제공하지 않는 개발자가 직접 만든 함수
    def get_file_name( self ):
        # 객체의 파일명을 가져옴
        return os.path.basename( self.file_upload.name )

    # 장고에서 제공하지 않는 개발자가 직접 만든 함수
    def get_file_ext(self):
        # 객체의 파일명을 가져와 확장자를 리턴
        return self.get_file_name().split( '.' )[ -1 ]
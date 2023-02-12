from django.contrib import admin
from .models import Post
# Register your models here.

# 장고 관리자 화면에서 Blog 앱안에 있는 Post모델을 관리할 수 있게 화면에 보여준다.
admin.site.register( Post )
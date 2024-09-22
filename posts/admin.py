from django.contrib import admin
from .models import Post,Comments
# Register your models here.

class CommentAdmininline(admin.TabularInline):
    model = Comments
    fields = ['کامنت']
    extra = 0
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','موضوع','ویلا','آپارتمان','زمین','اجاره','فروش','created_time']
    inlines = [CommentAdmininline]


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['id','post','کامنت','created_time']



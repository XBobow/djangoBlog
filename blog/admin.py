from django.contrib import admin
from .models import Category, Post, Tag, Sidebar
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Sidebar)



class PostAdmin(admin.ModelAdmin):
    ''' 文章详情管理 '''

    list_display = ('id', 'title','category', 'tags', 'pv', 'is_hot', 'pub_date', )
    search_fields = ('title', 'desc')
    list_editable = ('is_hot',)
    list_display_links = ('id', 'title',)

    class Media:
        css = {
            'all': ('ckeditor5/cked.css',)
        }

        js = (
            'https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js',
            'ckeditor5/ckeditor.js',
            'ckeditor5/translations/zh.js',
            'ckeditor5/config.js'
        )


admin.site.register(Post, PostAdmin)
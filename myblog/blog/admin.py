from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('pk', 'title', 'slug', )
    list_display_links = ('pk', 'slug', )
    search_fields = ('title', 'slug', )
    empty_value_display = "-пусто-"


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('pk', 'title', 'slug', )
    list_display_links = ('pk', 'slug', )
    search_fields = ('title', 'slug', )
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    # подключение класса через атрибут form, это для ckeditor
    # form = NewsAdminForm
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('pk', 'title', 'author', 'created_at', 'category', )
    list_display_links = ('pk', 'title')
    search_fields = ('title', 'author', )
    list_filter = ('author', 'created_at', 'category', )
    fields = ('title', 'slug', 'author', 'content', 'created_at', 'img', 'views', 'category', 'tags', )
    #  какие поля не редактируемые
    # readonly_fields = ('get_photo', 'cnt_views', 'created_at', 'updated_at')
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
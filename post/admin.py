from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from post.models import Tag, Category, Post
from ckeditor.widgets import CKEditorWidget




class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta :
        model = Post
        fields ='__all__'




@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Tag, TagAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'author', 'views', 'get_photo')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'author', 'category', 'content',
              'tags', 'views', 'photo', 'get_photo')
    list_filter = ('author', 'category', 'created_at')
    readonly_fields = ('views', 'get_photo',)
    form = PostAdminForm
    list_display_links = ('id', 'title')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'



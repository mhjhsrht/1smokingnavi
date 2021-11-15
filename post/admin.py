from django.contrib import admin
from tensorboard.plugins.custom_scalar.layout_pb2 import Category

from .models import Post, Comment, Category

admin.site.register(Post)
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
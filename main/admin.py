from django.contrib import admin
from django.contrib.auth import get_user_model

from main.models import Image, Recipe, Category, Comment


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 5


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]


admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Comment)

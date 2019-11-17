from django.contrib import admin

from .models import Technology, Category, Post


class TechnologyModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = Technology


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "technology"]

    class Meta:
        model = Category


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "publication_date", "last_modification_date"]

    class Meta:
        model = Post


admin.site.register(Technology, TechnologyModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)

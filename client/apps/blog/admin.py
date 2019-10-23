from django.contrib import admin

from .models import Comment, Post, Tag

def duplicate(modeladmin, request, queryset):

    for object in queryset:
        object.id = None
        if object.slug != '':
            object.slug = ''
        object.save()

duplicate.short_description = "Hacer un duplicado"

class CommentAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "timestamp", "object_id"]
    list_editable = ["object_id"]
    list_display_links = ["id"]
    list_filter = ["user"]
    search_fields = ["user", "content"]
    actions = [duplicate]

    class Meta:
        model = Comment


class PostAdmin(admin.ModelAdmin):

    list_display = ["user", "title", "slug", "draft"]
    list_display_links = ["user"]
    list_editable = ["title", "draft"]
    list_filter = ["user", "title", "tag"]
    search_fields = ["user", "title", "tag"]
    actions = [duplicate]

    class Meta:
        model = Post


class TagAdmin(admin.ModelAdmin):

    list_display = ["author", "title", "slug"]
    list_display_links = ["author"]
    list_editable = ["title"]
    list_filter = ["author"]
    search_fields = ["author", "title", "slug"]
    actions = [duplicate]

    class Meta:
        model = Tag


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
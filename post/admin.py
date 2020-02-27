# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


# Register your models here.
from BlogApp.models import Post,Category,Tag,Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)

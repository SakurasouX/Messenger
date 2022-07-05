from django.contrib import admin

from .models import Dialogue, Post, Comment, Image

admin.site.register(Dialogue)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)

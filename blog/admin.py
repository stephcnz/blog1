from django.contrib import admin

# Register your models here.
from .models import Post, authUser

admin.site.register(Post)
admin.site.register(authUser)
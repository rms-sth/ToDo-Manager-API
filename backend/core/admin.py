from django.contrib import admin

from .models import Category, ToDo, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(ToDo)

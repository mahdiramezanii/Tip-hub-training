from django.contrib import admin

from .models import Tag,BlogModel,Category


admin.site.register(Tag)
admin.site.register(BlogModel)
admin.site.register(Category)
from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date_posted',)

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
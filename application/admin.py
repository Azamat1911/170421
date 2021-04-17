from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('name','viewscounter')
    search_fields = ('name','content')

admin.site.register(models.Post,PostAdmin)

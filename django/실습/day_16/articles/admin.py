from django.contrib import admin
from .models import Articles,Comment
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comment)
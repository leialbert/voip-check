from atexit import register
from django.contrib import admin

from words.models import Word 

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('get_huashu','content','attachment','is_approved')

    @admin.display(description='话术')
    def get_huashu(self, obj):
        return obj.huashu.zhanghao
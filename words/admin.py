from atexit import register
from django.contrib import admin

from words.models import Word,Gateway

class GatewayInline(admin.StackedInline):
    model = Gateway.huashu.through
    # extra = 0

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('get_zhanghao','get_zhanghu','short_content','attachment','is_approved','created_at','updated_at')
    inlines = [GatewayInline,]

    @admin.display(description='账号')
    def get_zhanghao(self, obj):
        return obj.user_name.zhanghao
    @admin.display(description='账户')
    def get_zhanghu(self, obj):
        return obj.user_name.zhanghu
    

@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ('gateway_name','gateway_type')
from atexit import register
from django.contrib import admin

from words.models import Word,Gateway,Prefix

class GatewayInline(admin.TabularInline):
    model = Gateway.huashu.through
    # extra = 0
class PrefixInline(admin.StackedInline):
    model = Prefix
    extra = 0

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
    list_display = ('get_zhanghao','get_zhanghu','gateway_name','gateway_type')
    inlines = [PrefixInline,]
    @admin.display(description='账号')
    def get_zhanghao(self, obj):
        return obj.user_name.zhanghao
    @admin.display(description='账户')
    def get_zhanghu(self, obj):
        return obj.user_name.zhanghu

@admin.register(Prefix)
class PrefixAdmin(admin.ModelAdmin):
    list_display = ('get_gateway_name','callee_number','prefix_name')
    @admin.display(description='网关名称')
    def get_gateway_name(self,obj):
        return obj.related_gateway.gateway_name

from django.contrib import admin

from contracts.models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('get_zhanghao','get_zhanghu','company_title','company_license','company_address','is_license_ok','is_contract_ok','created_at','updated_at')

    @admin.display(description='账号')
    def get_zhanghao(self, obj:Contract):
        return obj.user_name.zhanghao
    @admin.display(description='账户')
    def get_zhanghu(self, obj:Contract):
        return obj.user_name.zhanghu
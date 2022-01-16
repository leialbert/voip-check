from django.contrib import admin

from contracts.models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('get_zhanghao','company_name','company_license','company_owner','contract_doc')

    @admin.display(description='账号')
    def get_zhanghao(self, obj):
        return obj.company_name.zhanghao

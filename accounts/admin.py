from pyexpat import model
from django.contrib import admin

from accounts.models import Account
from contracts.models import Contract

class ContractInline(admin.StackedInline):
    model = Contract
    extra = 0

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('zhanghao','zhanghu','balance','credit_amount','today_cost','kh_type')
    inlines = [ContractInline]
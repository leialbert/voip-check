from django.contrib import admin

from accounts.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('zhanghao','zhanghu','balance','credit_amount','today_cost')
from django.db import models

'''
账号信息数据来源于VOS的账户
@zhanghao 为VOS的账号（唯一的）
@zhanghu  为VOS的账户名称
@balance  为账户的余额
@credit_amount 为账户的透支额度
@today_cost 为当日消费情况
'''
class Account(models.Model):
    class Meta:
        verbose_name_plural = '账户信息'
    zhanghao = models.CharField('账号',max_length=40,unique=True)
    zhanghu = models.CharField('账户名称',max_length=40)
    balance = models.FloatField('账户余额')
    credit_amount = models.FloatField('透支额度') 
    today_cost = models.FloatField('今日消费')
    def __str__(self) -> str:
        return self.zhanghu

from random import choices
from django.db import models
class Account(models.Model):
    PTZH = 'PTZH'
    JSZH = 'JSZH'
    KH_CHOICES = [
        (PTZH,'普通账户'),
        (JSZH,'结算账户')
        ]
    zhanghao = models.CharField('账号',max_length=40,unique=True)
    zhanghu = models.CharField('账户名称',max_length=40)
    # balance = models.FloatField('账户余额',blank=True, null=True)
    # credit_amount = models.FloatField('透支额度',blank=True, null=True) 
    # today_cost = models.FloatField('今日消费',blank=True, null=True)
    kh_type = models.CharField('账户类型',max_length=20, choices=KH_CHOICES)
    created_at = models.DateTimeField('上传时间',auto_now_add=True)
    updated_at = models.DateTimeField('更新时间',auto_now=True)
    class Meta:
        verbose_name_plural = '账户信息'

    def __str__(self) -> str:
        return self.zhanghu

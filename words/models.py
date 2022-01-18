from django.db import models
from accounts.models import Account
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import truncatewords


# Create your models here.
class Word(models.Model):
    user_name = models.ForeignKey(Account,on_delete=CASCADE,verbose_name='关联用户')
    content = models.TextField('话术内容',max_length=1000,null=True,blank=True)
    @property
    def short_content(self):
        return truncatewords(self.content,10)
    attachment = models.FileField('附件',upload_to='words/',null=True,blank=True)
    is_approved = models.BooleanField('是否审核通过',default=False)
    created_at = models.DateTimeField('上传时间',auto_now_add=True)
    updated_at = models.DateTimeField('更新时间',auto_now=True)
    class Meta:
        verbose_name_plural = '话术报备'
    def __str__(self) -> str:
        return self.short_content

class Gateway(models.Model):
    DJWG = 'DJWG'
    LDWG = 'LDWG'
    GATEWAY_CHOICES = [
        (DJWG,'对接网关'),
        (LDWG,'落地网关')
        ]
    user_name = models.ForeignKey(Account,on_delete=CASCADE,verbose_name='关联用户')
    gateway_name = models.CharField('网关名称',max_length=30,unique=True)
    gateway_type = models.CharField('网关类型',max_length=40,choices=GATEWAY_CHOICES)
    huashu = models.ManyToManyField(Word,verbose_name='话术')
    class Meta:
        verbose_name_plural = '网关管理'
    
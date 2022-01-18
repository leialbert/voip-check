from django.db import models
from accounts.models import Account
from django.db.models.deletion import CASCADE
from datetime import datetime


# Create your models here.
class Word(models.Model):
    huashu = models.ForeignKey(Account,on_delete=CASCADE,verbose_name='话术')
    content = models.TextField('话术内容',max_length=1000,null=True,blank=True)
    attachment = models.FileField('附件',upload_to='words/',null=True,blank=True)
    is_approved = models.BooleanField('是否审核通过',default=False)
    created_at = models.DateTimeField('上传时间',auto_now_add=True)
    updated_at = models.DateTimeField('更新时间',auto_now=True)
    class Meta:
        verbose_name_plural = '话术报备'
    def __str__(self) -> str:
        return super().__str__()
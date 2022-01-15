from django.db import models
from accounts.models import Account
from django.db.models.deletion import CASCADE


# Create your models here.
class Contract(models.Model):
    class Meta:
        verbose_name_plural = '合同管理'
    company_name = models.ForeignKey(Account,on_delete=CASCADE,verbose_name='公司名称')
    company_license = models.FileField('营业执照',upload_to='contracts/company_license/',null=True)
    company_owner = models.FileField('法人',upload_to='contracts/person/',null=True)
    contract_doc = models.FileField('合同附件',upload_to='contracts/contract_doc/',null=True)
from django.db import models
from accounts.models import Account
from django.db.models.deletion import CASCADE


# Create your models here.
class Contract(models.Model):
    
    user_name = models.ForeignKey(Account,on_delete=CASCADE,verbose_name='关联账户',null=True)
    company_title = models.CharField('公司名称',max_length=40,null=True)
    company_license = models.CharField('税号',max_length=20,null=True)
    company_owner = models.CharField('法人',max_length=10,null=True)
    company_address = models.CharField('公司地址',max_length=40,null=True)
    company_license_doc = models.FileField('营业执照',upload_to='contracts/company_license/',null=True,blank=True)
    company_owner_doc = models.FileField('法人证件',upload_to='contracts/person/',null=True,blank=True)
    contract_doc = models.FileField('合同附件',upload_to='contracts/contract_doc/',null=True,blank=True)
    is_license_ok = models.BooleanField('证照齐全？',default=False)
    is_contract_ok = models.BooleanField('合同签署？',default=False)
    created_at = models.DateTimeField('上传时间',auto_now_add=True)
    updated_at = models.DateTimeField('更新时间',auto_now=True)
    class Meta:
        verbose_name_plural = '合同管理'

    def __str__(self) -> str:
        return super().__str__()

from django.db import models

# Create your models here.
class User(models.Model):

    

    # class Meta:
    #     verbose_name = "用户名"
    #     verbose_name_plural = "密 码"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
    
    username = models.CharField("用户名", max_length=128, unique=True)
    password = models.CharField("密码", max_length=256)
    mobilephone = models.CharField("手机号", max_length=11)
    update_time = models.DateTimeField(auto_now_add=True)
class Whiteip(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    whiteip = models.CharField("可信IP", max_length=128,unique=True)
    update_time = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

SEX_CHOICES = (
    (0, '男'),
    (1, '女'),
)
ROLE_CHOICES = (
    (0, 'buy'),
    (1, 'sale'),
    (2, 'admin')
)

BANK_CHOICES = (
    (0, '中国工商银行'),
    (1, '中国建设银行'),
    (2, '中国农业银行'),
    (3, '招商银行'),
    (4, '北京银行'),
    (5, '我家银行'),

)


# 用户表 Userinfo
class UserInfo(AbstractUser):
    realname = models.CharField(verbose_name='真实姓名', max_length=30, null=False)
    identity = models.CharField(verbose_name='身份证号', max_length=18, null=False)
    ads = models.CharField(verbose_name='地址', max_length=200, null=False)
    uphone = models.CharField(verbose_name='手机号', max_length=20, null=False)
    sex = models.IntegerField(verbose_name='性别', choices=SEX_CHOICES, default=0)
    role = models.IntegerField(verbose_name='角色', choices=ROLE_CHOICES, default=0)
    isActive = models.BooleanField(verbose_name='是否激活', default=False)
    isBan = models.BooleanField(verbose_name='是否禁用', default=False)

    def __str__(self):
        return self.username

#     用户名 username (C)
#     密码 password (C)
#     真实姓名 realname (C)
#     身份证号 identity (C)
#     住址 ads (C)
#     手机号 uphone (C)
#     性别 sex (Ic)
#     角色 : 卖家/买家 role (Ic)
#     激活状态 : 是否激活 isActive (B)
#     是否禁用 : isBan (B)


class Bank(models.Model):
    cardNo = models.CharField('卡号', max_length=30, null=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    cpwd = models.CharField('交易密码', max_length=200, null=False)
    bank = models.IntegerField(verbose_name='开户银行', choices=BANK_CHOICES, default=0)
    isDelete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.user.username
# 银行卡表 Bankinfo
#     卡号cardNo(C)
#     用户user(F)
#     交易密码cpwd(C)
#     开户银行bank(Ic)
#     是否删除isDelete(B)

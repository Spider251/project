from django.db import models
from userinfo.models import *

# Create your models here.

CAR_CHOISE = (
    (0, '审核中'),
    (1, '已审核'),
    (2, '未审核'),
    (3, '未通过'),
)


class Brand(models.Model):
    title = models.CharField('名称', max_length=50)
    logo = models.ImageField('logo', upload_to='img/logo', default='')
    newprice = models.DecimalField('新车价格', max_digits=8, decimal_places=2)
    isdelete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        return self.title


# 品牌表
# Brandinfo
# 名称
# title(C)
# logo
# logo(IM)
# 新车价格
# newprice(DE)
# 是否删除
# isdelete(B)

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    regist_data = models.DateField('上牌日期', null=False)
    engineNo = models.CharField('发动机号', max_length=50, null=False)
    mileage = models.IntegerField('公里数')
    record = models.CharField('维修记录', max_length=200)
    price = models.DecimalField('期望成功价格', max_digits=8, decimal_places=2)
    picture = models.ImageField('汽车图片', upload_to='img/car')
    formalities = models.BooleanField('手续是否齐全', default=True)
    debt = models.BooleanField('是否有债务', default=False)
    promise = models.TextField('卖家承诺', null=True)
    status = models.IntegerField('审核状态', choices=CAR_CHOISE, default=2)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    isDelete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.user.username

# 汽车表
# Carinfo
# 品牌
# brand(F)
# 上牌日期
# regist_data(DATA)
# 发动机号码
# engineNo(C)
# 公里数
# mileage(I)
# 维护记录
# record(C)
# 期望成功价格
# price(D)
# 图片
# picture(IM)
# 手续是否齐全
# formalities(B)
# 是否有债务
# debt(B)
# 卖家承诺
# promise(TEXT)
# 审核状态
# status(I)
# 用户user(F)
# 是否删除isDelete

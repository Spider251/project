from django.db import models
from userinfo.models import *
from sale.models import *

# Create your models here.
STATUS_CHOISE = (
    (0, '待支付'),
    (1, '已支付'),
    (2, '订单取消'),
    (3, '订单失败'),
    (4, '订单签收'),
)


class Cartinfo(models.Model):
    price = models.DecimalField('价格', max_digits=8, decimal_places=2)
    buser = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.buser.username


# 执行完表之后,不小心数据库中删除掉一张表,如何处理

class Orderinfo(models.Model):
    buser = models.ForeignKey(UserInfo, related_name='buser', on_delete=models.CASCADE)
    suser = models.ForeignKey(UserInfo, related_name='suser', on_delete=models.CASCADE)
    car = models.TextField('汽车')
    price = models.DecimalField('价格', max_digits=8, decimal_places=2)
    orderNo = models.CharField('订单号', max_length=50, null=False)
    status = models.IntegerField('订单状态', choices=STATUS_CHOISE, default=0)
    datatime = models.DateTimeField('时间', auto_now=True)
    isDelete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        return self.orderNo



from django.db import models

class User(models):
    use_name = models.CharField(max_length=50,
                            verbose_name='用户名')

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户user'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.use_name






class Sku(models):
    """
    商品表对应的内容,商品基本信息
    """
    # 名称
    name = models.CharField(max_length=50, verbose_name='名称')
    # 价格
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    # 进价
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='进价')
    # 市场价
    market_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='市场价')
    # 库存
    stock = models.IntegerField(default=0, verbose_name='库存')
    # 销量
    sales = models.IntegerField(default=0, verbose_name='销量')
    # 是否上架
    is_launched = models.BooleanField(default=True, verbose_name='是否上架销售')

    class Meta:
        db_table = 'tb_sku'
        verbose_name = '商品sku'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)


class ShopCar(models):
    """
    购物车表
    """
    # 用户id
    user_id = models.CharField(User,on_delete=models.CASCADE,verbose_name='名称')
    # 商品id
    sku_id = models.ForeignKey(Sku,on_delete=models.CASCADE,verbose_name='名称')
    # 数量
    count = models.IntegerField(verbose_name='个数')
    # 是否勾选
    selected = models.BooleanField(default=False, verbose_name='是否勾选')

    class Meta:
        db_table = 'tb_shopcar'
        verbose_name = '购物车shopcar'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_id


class OrderGoods(models):
    """
    订单商品
    """

    # 商品键
    sku = models.ForeignKey(Sku, on_delete=models.PROTECT, verbose_name="订单商品")
    # 数量
    count = models.IntegerField(default=1, verbose_name="数量")
    # 价格
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")


    class Meta:
        db_table = "tb_order_goods"
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name
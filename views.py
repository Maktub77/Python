from django.views import View


class ShopCarsView(View):

    def post(self, request):
        """接受数据  修改购物车数据 添加订单 和订单商品 加悲观锁 解决并发问题"""
        # 1.接收参数

        sku_ids = request.POST.get('sku_ids')


        # 2.判断是否登陆


        # 3.设置事务保存点


            # (3.1)捕获异常内容
            # 出现异常就回滚到tip初始位置

            # (3.2)获得购物车中每个商品的数量
            # if判断购物车里有没有该商品
            # 回滚到tip

            # (3.3)在商品表中 找该商品
            # 找不到就回滚到tip

            # (3.4)判断库存
            # 库存不足就回滚到tip

            # 添加订单商品表

        # 4.释放保存点


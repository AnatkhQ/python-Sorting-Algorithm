# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/12

""""""
"""
举例：
商品1：v 1 =60 w 1 =10
商品2：v 2 =100 w 2 =20
商品3：v 3 =120 w 3 =30
背包容量：W=50
"""
goods = [(60, 10),(100, 20),(120, 30)]  # 每个商品元组表示(价格, 重量)
goods.sort(key=lambda x: x[0]/x[1], reverse=True)  # 每克商品的价格进行排序


def fractional_backpack(goods, w):
    """
    分数背包
    :param goods: 商品列表
    :param w: 背包容量
    :return:
    """
    m = [0 for _ in range(len(goods))]  # [0,0,0] 对应商品个数
    total_v = 0  # 价值总数
    for i, (prize, weight) in enumerate(goods):
        print(m)
        if w >= weight:  # 当背包容量大于商品，继续拿
            m[i] += 1  # 拿到对应商品的个数，如果拿完了
            total_v += prize  # 增加价值
            w -= weight  # 减少容量
        else:  # 容量不够
            m[i] = w / weight  # 取商品的几分之几，实现尽量多拿贪心算法
            total_v += m[i] * prize  # 价值
            w = 0  # 拿完了，容量=0
            break
    return total_v, m

print(fractional_backpack(goods, 500))
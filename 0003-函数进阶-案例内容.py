#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time     : 2026/8/17 下午4:10
# @Author   : 陈李
# @File     :0003-函数进阶-案例内容.py
# @software :PyCharm

# #递归-> 函数自己调用自己，这是一个循环，需要一个终结点
# 定义以及分析，这是写代码前的两个重要部分
# 案例1：N的阶乘
def factorial(n):
    if n == 1:
        return 1  # 要想中断必须把判断放置在递归调用前面
    else:
        return n * factorial(n-1)


print(factorial(6))

"""
电商订单计算器
定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、
优惠（优惠券、折扣）、运费信息计算订单的总金额

"""
def calc_order_cost(*args, coupon=0, score=0, express=0):
    # 订单总金额 = 商品总金额 - 优惠券 - 折扣 + 运费
    """

    :param args: >(商品, 价格, 数量)
    :param coupon: 优惠券
    :param score: 积分折扣
    :param express: 运费
    :return: 订单总额
    """
    total_cost = sum([goods[1]*goods[2] for goods in args])

    if total_cost >= 5000:
        total_cost -= coupon

    if total_cost >= 5000 and score//100 <= 5000:
        total_cost -= score//100

    total_cost += express
    return total_cost # 在运行是发现，获得值为None，经过排查后发现原来是函数没有返回值，对于函数定义一定要注意要写下返回值

Order1 = calc_order_cost(("fruit", 100,1), ("Apple airpod", 9999, 1), ("computer", 10000, 1), coupon=2000, score=1000)
print(Order1)


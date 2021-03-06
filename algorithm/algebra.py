# -*- coding: utf-8 -*-
# 代数相关
# @author czhouyi@gmail.com


def get_median(num_list):
    """获取中位数，如果有两个中位数，取其平均值
    @author fancy
    """
    sort_list = sorted(num_list)
    middle = len(num_list) // 2
    if len(num_list) % 2 == 0:
        a = sort_list[middle]
        b = sort_list[middle - 1]
        return (a + b) / 2
    else:
        return sort_list[middle]


def get_mode(num_list):
    """获取众数，返回众数列表
    @author fancy
    """
    num_dic = {}
    for i in num_list:
        if num_dic.get(i) is None:
            num_dic[i] = 1
        else:
            num_dic[i] = num_dic[i] + 1
    max_count = max(num_dic.values())

    mode_list = []
    for k, v in num_dic.items():
        if v == max_count:
            mode_list.append(k)
    return mode_list


def get_gcd(a, b):
    """求两数的最大公约数
    """
    # todo 求两数的最大公约数
    return a


def is_prime(a):
    """判断是否质数
    """
    # todo 判断是否质数
    return True


def is_leap_year(year):
    """判断是否闰年

    能被400整除，或者能被4整除但不能被100整除的都是闰年
    """
    # todo 判断是否闰年
    return True

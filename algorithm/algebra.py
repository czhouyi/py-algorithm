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

# -*- coding: utf-8 -*-
# 字符相关
# @author czhouyi@gmail.com


def reverse(input_str):
    """反转字符串
    """
    result_list = []
    for i in range(len(input_str) - 1, -1, -1):
        result_list.append(input_str[i])
    return ''.join(result_list)

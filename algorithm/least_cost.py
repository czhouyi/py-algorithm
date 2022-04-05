"""
每个用户有三个策略，消耗分别为user_list[0],user_list[1],user_list[2]
每个用户选择一个策略执行，相邻用户不能选择相同策略
求user_list总体的最小消耗
"""


def least_cost(user_list):
    min_a, min_b, min_c = 0, 0, 0
    for i in range(len(user_list)):
        a, b, c = min_a, min_b, min_c
        min_a = min(user_list[i][0] + b, user_list[i][0] + c)
        min_b = min(user_list[i][1] + a, user_list[i][1] + c)
        min_c = min(user_list[i][2] + a, user_list[i][2] + b)
    return min(min_a, min_b, min_c)

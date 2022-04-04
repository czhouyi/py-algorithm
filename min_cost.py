def min_cost(user_list):
    min_choose = [0, 0, 0]
    for i in range(len(user_list)):
        a = min_choose[0]
        b = min_choose[1]
        c = min_choose[2]
        min_choose[0] = min(user_list[i][0] + b, user_list[i][0] + c)
        min_choose[1] = min(user_list[i][1] + a, user_list[i][1] + c)
        min_choose[2] = min(user_list[i][2] + a, user_list[i][2] + b)
    return min(min_choose[0], min_choose[1], min_choose[2])


if __name__ == '__main__':
    cc = [[5, 7, 9], [6, 1, 3], [4, 2, 8]]
    print(min_cost(cc))

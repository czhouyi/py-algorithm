def get_mode(num_list):
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


if __name__ == '__main__':
    input_list = [1, 1, 5, 4, 6, 66, 6, 8, 8, 8, 9, 97, 0]
    print(get_mode(input_list))

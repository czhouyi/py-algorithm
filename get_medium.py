def get_median(num_list):
    sort_list = sorted(num_list)
    middle = len(num_list) // 2
    if len(num_list) % 2 == 0:
        a = sort_list[middle]
        b = sort_list[middle - 1]
        return (a + b) / 2
    else:
        return sort_list[middle]


if __name__ == '__main__':
    input_list = [1, 1, 5, 4, 6, 66, 6, 8, 8, 8, 9, 97, 0]
    print(get_median(input_list))

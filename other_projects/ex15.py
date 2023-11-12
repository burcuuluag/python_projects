
def sorted_by_key(my_dict):
    my_keys = list(my_dict.keys())
    my_keys.sort()

    sorted_dict = {}
    for i in my_keys:
        sorted_dict[i] = my_dict[i]
    print(sorted_dict)


if __name__ == '__main__':
    my_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
    sorted_by_key(my_dict)
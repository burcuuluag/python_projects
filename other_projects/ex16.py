
def sorted_keys():
    key_value = {}

    key_value[2] = '56'
    key_value[1] = '2'
    key_value[4] = '12'
    key_value[5] = '24'
    key_value[6] = '18'
    key_value[3] = '323'

    #print(key_value)

    sorted_key_dict = {}

    for key in sorted(key_value.keys()):
        sorted_key_dict[key] = key_value[key]
    print(sorted_key_dict)


if __name__ == '__main__':
    sorted_keys()

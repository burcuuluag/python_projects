
# sözlükten name'i silme:

def pop_name_key():
    my_info = {'name': 'Burcu', 'surname': 'Uluag', 'age': 29}

    my_info.pop("name")
    return my_info


if __name__ == '__main__':
    result = pop_name_key()
    print(result)
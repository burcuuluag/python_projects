
# sözlükten yasini guncelle:

def update_age():
    my_info = {'name': 'Burcu', 'surname': 'Uluag', 'age': 29}

    my_info.pop("age")

    my_info["age"] = 28
    return my_info


if __name__ == '__main__':
    result = update_age()
    print(result)
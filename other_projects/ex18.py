

# sözlükteki name değerine eriş (Burcu yazdır!)

def get_name_from_dict():
    my_info = {
        "isim": "John",
        "yas": 25,
        "meslek": "Muhendis",
        "sehir": "New York"
    }

    print(my_info["isim"])

    # Or

    isim = my_info["isim"]
    print(isim)

if __name__ == '__main__':
    get_name_from_dict()
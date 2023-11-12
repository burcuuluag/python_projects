
# verilen bir listeden elemanları tek tek alıp başka bir listeye ekle:

def combine_list(list1):
    my_list = []
    for item in list1:
        for i in item:
            my_list.append(i)
    return my_list


if __name__ == "__main__":
    list1 = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
    result = combine_list(list1)
    print(result)


# my_list = [i for item in list1 for i in item]
# birinci listede bulunup ikinci listede bulunmayan rakamların karesinden oluşan bir liste oluşturalım..

def convert_to_list(list1, list2):
    my_list = []
    for i in list1:
        if i not in list2:
            my_list.append(i*i)
    return my_list


if __name__ == "__main__":
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = [2,3,6,9,5]
    result = convert_to_list(list1, list2)
    print(result)

#my_list = [i*i for i in list1 if i not in list2]
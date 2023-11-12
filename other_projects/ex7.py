
def find_missing_number():
    my_list = [1,2,4,5,6,7]

    my_list.sort()
    print(my_list)
    max_number = max(my_list)
    
    for i in my_list:
        a = i + 1
        if a in my_list:
            continue
        elif i == max_number:
            break
        else:
            print("missing number:", a)


if __name__ == '__main__':
    find_missing_number()
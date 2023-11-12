
def creat_numbers_and_letters_tuple(numbers, letters):
    my_tuple_list = []
    for i in numbers:
        for j in letters:
            my_tuple_list.append((i,j))

    return my_tuple_list


if __name__ == '__main__':
    numbers = [1,2,3,4]
    letters = "abcd"
    result = creat_numbers_and_letters_tuple(numbers, letters)
    print(result)


## list comprehension nasıl yapılırdı:
##def creat_numbers_and_letters_tuple(numbers, letters):
##    my_list = [(i,j) for i in numbers for j in letters]
##    return my_list
##
##if __name__ == '__main__':
##    numbers = [1,2,3,4]
##    letters = "abcd"
##    result = creat_numbers_and_letters_tuple(numbers, letters)
##    print(result)
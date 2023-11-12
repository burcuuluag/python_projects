# verilen listede 4 den büyük çift sayıların karelerininden oluşan bir liste yap:

def even_number(numbers):
    even_number = []
    for i in numbers:
        if i > 4 and i %2 == 0:
            even_number.append(i*i)

    return even_number

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9]
    result = even_number(numbers)
    print(result)


# list comprehensions şeklinde yapımı:
#def even_number(numbers):
#    even_number = [i*i for i in numbers if i > 4 and i %2 == 0]
#    return even_number
#
#if __name__ == '__main__':
#    numbers = [1,2,3,4,5,6,7,8,9]
#    result = even_number(numbers)
#    print(result)
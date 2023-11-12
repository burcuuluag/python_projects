
def even_number(numbers):
    even_number = []
    for i in numbers:
        if i %2 == 0:
            num = i * i
            even_number.append(num)

    return even_number

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9]
    result = even_number(numbers)
    print(result)




def given_sum_value_of_array(arr, sum):
    for i in arr:
        for j in arr:
            if i + j == sum:
                print(i, j)
            else:
                continue


if __name__ == '__main__':
    arr = [5,7,4,3,9,8,19,21]
    sum = 17
    given_sum_value_of_array(arr, sum)

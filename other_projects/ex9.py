from itertools import permutations

def list_comprehensions(x,y,z,n):
    my_list = [x,y,z]
    p = permutations(my_list)

    for i in list(p): 
        print(i) 


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_comprehensions(x,y,z,n)
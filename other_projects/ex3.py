

def convert_to_dict():
    list1 = ["Naina", "Kimi", "Sheena"]
    list2 = [123, 456, 789]

    res = dict(map(lambda i,j : (i,j), list1, list2))
    print(res)

convert_to_dict()
def viralAdvertising(n):
    cumulative = []

    l = 5 // 2
    cumulative.append(l)
    
    for i in range(1, n):
        s = l * 3
        l = s // 2
        c = cumulative[-1] + l
        cumulative.append(c)

    output = cumulative[-1]
    return output

if __name__ == '__main__':
    n = int(input("bir sayi gir: "))
    print(type(n))
    result = viralAdvertising(n)
    print(result)
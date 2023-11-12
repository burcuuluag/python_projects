def common_letters(text1, text2):
    common_letters = []
    for i in text1:
        for j in text2:
            if i == j:
                if i not in common_letters:
                    common_letters.append(i)
                else:
                    pass
            else:
                continue

    print(common_letters)


if __name__ == '__main__':
    text1 = "NAINA"
    text2 = "REENE"
    common_letters(text1, text2)
    
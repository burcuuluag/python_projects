
def common_words(text):
    words = text.split(" ")
    my_dict = {}

    for i in words:
        my_dict[i]=my_dict.get(i, 0) + 1
    print(my_dict)


if __name__ == '__main__':
    text = "she is a beautiful. she is an awful."
    common_words(text)
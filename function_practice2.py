def filter_long_words(words,mainlangth=5):
    filterd_list=[]
    for word in words :
        if len(word) >= mainlangth :
            filterd_list.append(word)
    return filterd_list

word_list = ["python","c","java","functions","git"]
print(filter_long_words(word_list))
print(filter_long_words(word_list,4))

    
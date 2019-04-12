def get_middle(s):
    s_len = len(s)
    print(s_len)
    if s_len % 2 != 0:
        word_place = int((s_len / 2))
        word = s[word_place]
        print(word)
    elif s_len % 2 == 0:
        word_1_place = int(s_len / 2) - 1
        word_2_place = int((s_len / 2))
        word_1 = s[word_1_place]
        word_2 = s[word_2_place]
        print(word_1 + word_2)


get_middle('A')

#Better solution with slice notation:
def get_middle(s):
    print(s[(len(s)-1)//2:len(s)//2+1])


get_middle('test')
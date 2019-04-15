def get_sum(a, b):
    lst = [a, b]
    lst.sort()
    # print(lst)

    if a == b:
        # print(a)
        return a
    elif lst[0] == lst[1]-1:
        # print(a + b)
        return a + b
    elif a != b:
        suma = 0
        for i in range(lst[0], lst[1]+1):
            # print(i)
            suma += i
        print(suma)
        return suma


get_sum(-1, 2)


# better solution
def get_sum(a, b):
    return sum(range(min(a, b), max(a, b)+1))

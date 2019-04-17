from itertools import permutations
# python 不能传入比较器，不知道该如何实现多个str[]传入的排序
# 这个只是实现了传入一个str，按字典序的排序
def Lowest_string(str):
    if str == None or len(str) == 0:
        return ''

    sort_str = list(permutations(str))
    return sort_str


if __name__ == '__main__':
    print(Lowest_string("abc"))
# while True:
#     try:
#         num = int(input())
#         arr = []
#         for i in range(1, num):
#             Sum = 0
#             # 超过这个数的一半就不可能被整除了，所以后一半就不用考虑
#             for j in range(1, i // 2 + 1):
#                 # 如果能整除，就加进去
#                 if i % j == 0:
#                     Sum += j
#             # 加完之后判断和是不是等于这个数，不包括1
#             if Sum == i and i != 1:
#                 arr.append(i)
#         print(len(arr))
#     except:
#         break

import math


def isperfect(num):
    if num == 1:
        return 0
    else:
        elements = []

        # sqrt方法就是求num一半的数
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                elements.append(i)
                # 如果num能被这个数整除，并且被整除后得到的结果不是1或者num本身，就加进去
                # 例如num = 6时，1，2，3就会被加进去
                if (num / i) != i and (num / i) != num:
                    elements.append((num / i))
        # 加完之后看和等不等与num（6）
        if sum(elements) == num:
            return 1
        else:
            return 0


while True:
    try:
        N = int(input())
        count = 0

        for n in range(1, N):
            count = count + isperfect(n)

        print(count)
    except:
        break
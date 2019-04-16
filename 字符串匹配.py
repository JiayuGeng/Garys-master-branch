# 判断一个str在不在另一个str里面

# while True:
#     try:
#         str1 = set(input())
#         str2 = set(input())
#         if str1 & str2 == str1:
#             print('true')
#         else:
#             print('false')
#
#     except:
#         break

# 正则匹配字符串 *？
while 1:
    try:
        first = input()
        second = input()

        a, b, k = 0, 0, 1

        # 到倒数第二个停止
        while a < len(first) - 1 and b < len(second) - 1:
            if first[a] == second[b] or first[a] == '?':
                a += 1
                b += 1
            # 当碰到'*'，就继续从它下一个开始看
            elif first[a] == '*':
                # 如果first中a的下一个=second中b的下一个，或者没下一个了
                if first[a + 1] == second[b + 1] or not first[a + 1] or not second[b + 1]:
                    a += 1
                    b += 1
                # 如果first中a的下一个不等second中b的下一个，说明还是在*的匹配内，那么b+=1，目的是看结束时，能否全是*全匹配上
                else:
                    b += 1
            else:
                k = 0
                break

        if k == 1:
            print('true')
        else:
            print('false')
    except:
        break

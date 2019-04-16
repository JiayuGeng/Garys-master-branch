while True:
    try:
        first_str = 'helhello'
        second_str = 'worhello'

        index = 0

        if len(first_str) > len(second_str):
            first_str, second_str = second_str, first_str

        for i in range(len(first_str) + 1):
            # 当index找到当前最长的公共子串时就不动了，但是i依旧在移动此时再通过i-index：i从头进行比较
            # 这样的好处是，当超过之前index停留的位置后，说明长度就比之前的子串长，就可以覆盖之前的短的了
            if first_str[i - index: i] in second_str:
                res = first_str[i - index: i]
                index += 1
        print(res)
    except:
        break
'''
找最长公共子串的长度：
'''
# while True:
#     try:
#         str1 = input()
#         str2 = input()
#
#         index = 0
#         if len(str1) > len(str2):
#             str1, str2 = str2, str1
#
#         for i in range(len(str1)):
#             if str1[i - index: i + 1] in str2:
#                 index += 1
#         print(index)
#     except:
#         break
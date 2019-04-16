# Manacher 算法
# 51ABBA -> 4

# def Manacher_String(str):
#     chaArr = [i for i in str]
#     res = []
#     for i in chaArr:
#         res.append('#')
#         res.append(i)
#     res.append('#')
#     return res
#
# def Max_Lcps_length(str):
#     charArr = Manacher_String(str)
#     pArr = [None] * len(charArr)
#     R = -1
#     C = -1
#     Max = 0
#
#     for i in range(len(charArr)):
#         if R > i:
#             pArr[i] = min(pArr[2 * C - i], R - i)
#         else:
#             pArr[i] = 1
#
#         while i + pArr[i] < len(charArr) and i - pArr[i] > -1:
#             if charArr[i + pArr[i]] == charArr[i - pArr[i]]:
#                 pArr[i] += 1
#             else:
#                 break
#         if i + pArr[i] > R:
#             R = i + pArr[i]
#             C = i
#
#         Max = max(Max, pArr[i])
#     return Max - 1
#
# while True:
#     try:
#         print(Max_Lcps_length(input()))
#     except:
#         break


def longestPalindrome(s):
    if s == s[::-1]:
        return len(s)
    maxLen = 0
    for i in range(len(s)):
        # 考虑的是maxLen定住，i增加的情况
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            maxLen += 2
            continue
        # 考虑的是i与maxLen同时增加的情况
        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            maxLen += 1
    return maxLen


while True:
    try:
        a = input()
        if a:
            print(longestPalindrome(a))

    except:
        break
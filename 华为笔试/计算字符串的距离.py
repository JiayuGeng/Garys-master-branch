def editDistance(str1, str2):
    len1, len2 = len(str1) + 1, len(str2) + 1
    dp = [[0 for _ in range(len2)] for _ in range(len1)]
    for i in range(len1):
        dp[i][0] = i
    for j in range(len2):
        dp[0][j] = j
    for i in range(1, len1):
        for j in range(1, len2):
            # 当前数字从dp[1][1]开始，当前数字的值=min(它左边的值+1；它上边的值+1；它左上角的值+如果两个字符串比较相等则加1，否则加0)
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
    return dp[-1][-1]


while True:
    try:
        print(editDistance(input(), input()))
    except:
        break

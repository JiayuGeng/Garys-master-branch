import bisect

'''
首先计算每个数在最大递增子串中的位置
186 186 150 200 160 130 197 200 quene
1 1 1 2 2 1 3 4 递增计数

然后计算每个数在反向最大递减子串中的位置--->计算反向后每个数在最大递增子串中的位置
200 197 130 160 200 150 186 186 反向quene
1 1 1 2 3 2 3 3 递减计数

然后将每个数的递增计数和递减计数相加
186 186 150 200 160 130 197 200 quene
1 1 1 2 2 1 3 4 递增计数
3 3 2 3 2 1 1 1 递减计数
4 4 3 5 4 2 4 5 每个数在所在队列的人数+1（自己在递增和递减中被重复计算）

如160这个数
在递增队列中有2个人数
150 160
在递减队列中有2个人数
160 130
那么160所在队列中就有3个人
150 160 130
每个数的所在队列人数表达就是这个意思
总人数 - 该数所在队列人数 = 需要出队的人数

'''

def process(arr, dp):
    b = [9999] * len(arr)
    for i in range(len(arr)):
        # 找到arr[i]应该插入到b的位置，保持递增序，但是只是找到位置记录成pos，先不插入
        pos = bisect.bisect_left(b, arr[i])
        dp += [pos + 1]
        # 现在插入arr[i]，为了后续的计算
        b[pos] = arr[i]

    return dp

while True:
    try:
        num = int(input())
        arr = list(map(int, input().split()))
        dp1 = []
        dp2 = []

        dp1 = process(arr, dp1)
        # dp1记录的是每个数在最大递增子串中的位置：[1, 1, 1, 2, 2, 1, 3, 4] 递增计数
        # 把arr逆序求dp2
        arr2 = arr[::-1]
        # 求的结果在反过来
        dp2 = process(arr2, dp2)[::-1]
        # dp2记录的是每个数反向最大递减子串中的位置：[1 1 1 2 3 2 3 3] 递减计数
        # dp2个数组相加，找出最大的值
        res = max(dp1[i] + dp2[i] for i in range(len(arr)))
        # 用输入的人数 - 最大的值 + 1则是结果
        print(num - res + 1)

    except:
        break


# def process(arr):
#     dp = [None] * len(arr)
#     for i in range(len(arr)):
#         dp[i] = 1
#         for j in range(i):
#             # 如果i之前的数都小于i，那么i之前的数都可以作为倒数第二个数
#             # 在这么多倒数第二个数的选择中，以哪个数结尾的递增子序列更大，就选哪个数作为倒数第二个数
#             # 如果i之前的数都>=i，那么直接让dp[i] = 1即可，说明以arr[i]结尾的情况下最长的递增子序列只有arr[i]
#             if arr[i] > arr[j]:
#                 # dp[j] + 1意思是dp[j]作为倒数第二个数，再加上倒数第一个数dp[i]，代表最长递增子序列的长度
#                 dp[i] = max(dp[i], dp[j] + 1)
#
#     return dp

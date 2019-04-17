from heapq import *
# 切金条满足条件并最少花费
# 小根堆求出最小花费

def Least_Money(arr):
    pQ = []
    for i in range(len(arr)):
        heappush(pQ, arr[i]) # 或者heapify也可以，直接形成小根堆
    print(pQ)

    Sum = 0
    while len(pQ) > 1:
        # heappop 就是从堆中弹出最小的值
        cur = heappop(pQ) + heappop(pQ) # 一直找小根堆中最小的2个数的和，算完加入堆
        Sum += cur                      # 就是小根堆
        heappush(pQ, cur)
    return Sum

if __name__ == '__main__':
    print(Least_Money([7,6,3,2,4,5,1]))
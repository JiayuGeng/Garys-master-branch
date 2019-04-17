# 就是找最左侧>=某个数的位置是多少

import math

def BSNearLeft(arr, num):
    L = 0
    R = len(arr) - 1
    index = -1
    while L < R:
        mid = L + math.ceil((R - L) / 2) # 这里得用向上取整
        if arr[mid] >= num:
            index = mid # 记录每次的index，>=这种判断一定会包括最终答案
            R = mid - 1
        else:
            L = mid + 1
    return index

def main():
    print(BSNearLeft([1,3,4,5,7,8,12,34,67,78,99], 4))

if __name__ == '__main__':
    main()
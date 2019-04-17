import math

def smallSum(arr):
    if arr == None or len(arr) < 2:
        return 0
    process(arr, 0, len(arr) - 1)

    return res


def process(arr, l, r):
    if l == r:
        return 0
    mid = math.floor(l + (r - l) / 2)

    # 返回左侧部分产生小和+右侧小和+两边和起来
    return process(arr, l, mid) + process(arr, mid + 1, r) + merge(arr, l, mid, r)

def merge(arr, l, m, r):
    global res

    help = [0] * (r - l + 1)
    i = 0 # help数组的指针
    p1 = l  # 左侧部分的下标
    p2 = m + 1  # 右侧部分的下标
    res = 0

    while p1 <= m and p2 <= r:
        # 如果左侧小于右侧，就产生r - p2 + 1个小和，就说明右侧有r - p2 + 1个数比左侧数大，再乘左侧的数
        if arr[p1] < arr[p2]:
            # 把小和累加
            res += (r - p2 + 1) * arr[p1]
            # help数组copy小的数
            help[i] = arr[p1]
            i += 1
            p1 += 1

        else: # 左侧与右侧相等，拷贝右侧部分的
            help[i] = arr[p2]
            i += 1
            p2 += 1

    while p1 <= m:  # p1不越界，把p1剩下部分copy到help
        help[i] = arr[p1]
        i += 1
        p1 += 1

    while p2 <= r:  # p2不越界，把p2剩下部分copy到help
        help[i] = arr[p2]
        i += 1
        p2 += 1

    # 最后再把help数组里的数copy到原arr数组里
    for i in range(len(help)):
        arr[l + i] = help[i]

    return res



def main():
    print(smallSum([1,3,4,5,6,0]))


if __name__ == '__main__':
    main()

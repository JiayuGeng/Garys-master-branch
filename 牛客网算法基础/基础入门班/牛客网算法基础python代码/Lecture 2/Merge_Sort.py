import math

def mergeSort(arr):
    if arr == None or len(arr) < 2:
        return
    process(arr, 0, len(arr) - 1)

    return arr

# arr[l...r]范围上调整成有序的
def process(arr, l, r):
    if l == r: # 上面只有一个数，不用做任何调整，本来就有序
        return
    mid = math.floor(l + (r - l) / 2)
    process(arr, l ,mid) # arr[l...mid]左侧部分让它有序
    process(arr, mid + 1, r) # arr[mid+1...r]右侧部分让它有序
    merge(arr, l, mid, r)

# merge 2 arr
def merge(arr, l, m, r):
    help = [0] * (r - l + 1)
    i = 0
    p1 = l # 左侧部分的下标
    p2 = m + 1 # 右侧部分的下标

    while p1 <= m and p2 <= r: # p1不越界且p2也不越界
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            i += 1
            p1 += 1
        else:
            help[i] = arr[p2]
            i += 1
            p2 += 1
     # p1 p2 一定有一个越界，另一个不越界

    while p1 <= m: # p1不越界，把p1剩下部分copy到help
        help[i] = arr[p1]
        i += 1
        p1 += 1

    while p2 <= r: # p2不越界，把p2剩下部分copy到help
        help[i] = arr[p2]
        i += 1
        p2 += 1

    for i in range(len(help)):
        arr[l + i] = help[i]

def main():
    print(mergeSort([1,3,4,5,6,0]))

if __name__ == '__main__':
    main()

'''
递归排序思想：先一路一直给这组数据二分，直到不能再分，开始往上返回每个子树中较大的值
笔记有详细解释
'''

def getMax(arr):
    return process(arr, 0, len(arr) - 1)

def process(arr, L, R):
    if L == R:
        return arr[L]
    mid = int(L + (R - L) / 2)
    Left_max = process(arr, L, mid)
    Right_max = process(arr, mid + 1, R)

    return max(Left_max, Right_max)

def main():
    print(getMax([1,2,3,4,5]))

if __name__ == '__main__':
    main()
'''
局部最小：给个arr，任意相邻2个数无顺序，找局部最小值的index

思路：
先看0位，是min则输出，不是在看最后2位，是则输出，不是再找mid
如果mid是min，则输出mid，如果mid不是的话，
如果mid > left num，说明左边一定存在局小
如果mid > right num，那么右边一定存在局小
如果mid > both，那么左右两边一定都存在局小
哪边存在局小，接着打mid二分哪边，直到找到
'''
def getLessIndex(arr):
    if arr == None or len(arr) == 0:
        return -1
    if len(arr) == 1 or arr[0] < arr[1]:
        return 0
    if arr[len(arr) - 1] < arr[len(arr) - 2]:
        return len(arr) - 1

    left = 1
    right = len(arr) - 2

    while left < right:
        mid = int(left + (right -left) / 2)
        if arr[mid] > arr[mid - 1]: # mid > mid左边数，说明局小在mid左侧
            right = mid - 1 # mid的右边就不考虑了
        elif arr[mid] > arr[mid + 1]: # mid > mid右边数，说明局小在mid右侧
            left = mid + 1 # mid左边就不考虑了
        else:
            # mid既不大于mid左，又不大于mid右，就说明mid是局小，返回mid
            return mid

    return left

def main():
    print('The less number index is {}'.format(getLessIndex([5,6,1,7,8])))

if __name__ == '__main__':
    main()

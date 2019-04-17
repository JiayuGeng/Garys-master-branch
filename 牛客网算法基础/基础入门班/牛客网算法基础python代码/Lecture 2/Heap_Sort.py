
# 大根堆
# index位置上是新加的数，或者是变大的数
# 重新调成大根堆
def Heap_Insert(arr, index):
    # 子比父大了
    while arr[index] > arr[int((index - 1) / 2)]:
        # 父与子交换
        arr[index], arr[int((index - 1) / 2)] = arr[int((index - 1) / 2)], arr[index]
        index = int((index - 1) / 2)

def Heap_Sort(arr):
    if arr == None or len(arr) < 2:
        return

    for i in range(len(arr)):
        Heap_Insert(arr, i)
    # 最开始输入的arr是 [1,2,4,1,1,3]
    # 现在数组整体是大根堆了 [4,1,3,1,1,2]
    # 堆的有效size
    heapSize = len(arr)
    # 最大值和数组最后一个数做交换，size - 1
    arr[0], arr[heapSize - 1] = arr[heapSize - 1], arr[0]
    heapSize -= 1

    while heapSize > 0:
        Heapify(arr, 0, heapSize)
        arr[0], arr[heapSize - 1] = arr[heapSize - 1], arr[0]
        heapSize -= 1

    return arr


# arr[i] 位置的值发生了变化，并且是变小，堆大小是heapSize(arr[0 ~ heapSize - 1])
# 堆只能向下调整，重新调成大根堆
def Heapify(arr, i, heapSize):
    # 左孩子位置
    L = int(i * 2 + 1)
    # 左孩子不越界，执行while，就是i位置往下有无孩子？
    while L < heapSize:
        # L + 1 —>（右孩子）如果有右孩子，并且值比左孩子大，就把右孩子给largest，否则左孩子给largest
        # 就是看左右两个孩子谁大，谁给largest
        if L + 1 < heapSize and arr[L + 1] > arr[L]:
            largest = L + 1
        else:
            largest = L

        # 两个孩子较大的值和父节点的值比较，最大值的下标作为largest的值
        # 两个孩子和父pk，这三者谁大谁给largest
        if arr[largest] <= arr[i]:
            largest = i

        # 如果最大值的坐标已经是父节点的位置，停止
        if largest == i:
            break

        # 选出来largest的位置一定不是i位置，是i位置左右两个孩子中，较大数的下标
        # 父节点的值与我较大孩子做交换
        arr[i], arr[largest] = arr[largest], arr[i]
        # 我来到了我原来较大孩子的位置
        i = largest
        # 左孩子重新往下走一个
        L = int(i * 2 + 1)


if __name__ == '__main__':
    print(Heap_Sort([1,2,4,1,1,3]))

# 思路就是i从第0位开始，j从i后面开始，通过j每次找到最小的值放在i位置，i++

def SelectionSort(arr):
    if arr == None or len(arr) < 2:
        return
    # print('原arr：', arr)
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        # print('第{}次交换后的Arr：'.format(i + 1), arr)


    return arr

def main():
    print(SelectionSort([4,3,6,1,5]))

if __name__ == '__main__':
    main()

'''
原arr： [4, 3, 6, 1, 5]
第1次交换后的Arr： [1, 3, 6, 4, 5]，第一位之前就不再动了，排好了
第2次交换后的Arr： [1, 3, 6, 4, 5]，第二位之前就不再动了，排好了
第3次交换后的Arr： [1, 3, 4, 6, 5]
第4次交换后的Arr： [1, 3, 4, 5, 6]
[1, 3, 4, 5, 6]
'''
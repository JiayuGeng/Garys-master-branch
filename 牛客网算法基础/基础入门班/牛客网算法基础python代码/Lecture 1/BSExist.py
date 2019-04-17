'''
二分法前提必须有序
'''

def BSExist(arr, num):
    if arr == None or len(arr) == 0:
        return False

    L = 0
    R = len(arr) - 1
    while L < R: # 当L和R相等时，说明所有数字已经遍历完了，在判断他俩相等的数字是不是num，是的话，True
        mid = int(L + (R - L) / 2)
        if arr[mid] == num:
            return True
        elif arr[mid] > num: # 如果mid大于要找的数，mid右边的数直接不看了，R直接变到mid左边的数
            R = mid - 1
        else:
            L = mid + 1

    if arr[L] == num: # 在这里判断他俩相等的数字是不是num，是的话，True
        return True
    else:
        return False

def main():
    print(BSExist([1,2,4,5,8,10,11,12], 4))

if __name__ == '__main__':
    main()
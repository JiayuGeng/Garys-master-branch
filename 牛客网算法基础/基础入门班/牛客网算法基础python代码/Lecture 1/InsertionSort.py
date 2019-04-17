
def InsertionSort(arr):
    if arr == None or len(arr) < 2:
        return

    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    print(InsertionSort([45,23,67,100,56,29]))

if __name__ == '__main__':
    main()

'''
注意不能arr[j - 1]和arr[j]比较，因为第0位-1就变成arr[-1]，就直接与最后一位交换了，
只能arr[j]和arr[j + 1]比较
'''
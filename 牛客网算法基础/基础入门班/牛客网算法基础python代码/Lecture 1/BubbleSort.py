
def BubbleSort(arr):
    if arr == None or len(arr) < 2:
        return

    for i in range(len(arr) - 1, 0, -1): # 控制最后一个数之前排好序，然后最后一个数就不再动，开始到倒数第二个数...
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    print(BubbleSort([45,78,23,67,90,12]))

if __name__ == '__main__':
    main()
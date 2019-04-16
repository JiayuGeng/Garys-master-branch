while 1:
    try:
        num1 = int(input())
        arr1 = list(map(int, input().split()))
        num2 = int(input())
        arr2 = list(map(int, input().split()))

        arr = arr1 + arr2
        print(''.join(list(map(str, sorted(list(set(arr)))))))
    except:
        break
while True:
    try:
        num = int(input())
        def isprime(num):
            if num == 1:
                return False
            elif num == 2:
                return True
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

        for i in range(num // 2, num):
            # i就是中间数，就是从中间往两边扩着找
            if isprime(i) and isprime(num - i):
                print(num - i)
                print(i)
                break
    except:
        break
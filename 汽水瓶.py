import sys

while True:
    empty = sys.stdin.readline().strip()
    if empty == '0':
        break
    empty = int(empty)
    res = 0

    while empty >=2:
        if empty == 2:
            res += 1
            break

        drink = empty // 3
        empty = empty % 3
        res += drink
        empty += drink

    print(res)

'''
while True:
    try:
        print(int(input()) // 2)
    except:
        break
'''
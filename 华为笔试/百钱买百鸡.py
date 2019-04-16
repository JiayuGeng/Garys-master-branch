while True:
    try:
        a = input()
        '7x + 4y = 100 '
        '=> 0 <= x <= 14, 0 <= y <= 25'
        for x in range(15):
            for y in range(26):
                if 7 * x + 4 * y == 100:
                    z = 100 - x - y
                    print('{} {} {}'.format(x, y, z))
    except:
        break
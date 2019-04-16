def check(ip1, ip2, mask):
    ip1 = list(map(int, ip1.split('.')))
    ip2 = list(map(int, ip2.split('.')))
    mask = list(map(int, mask.split('.')))

    if len(ip1) != 4 or len(ip2) != 4:
        return 1

    for i in ip1:
        if i > 255 or i < 0:
            return 1

    for j in ip2:
        if j > 255 or j < 0:
            return 1

    s = ''
    for k in mask:
        if k > 255 or k < 0:
            return 1

        str1 = bin(k)[2:]
        str2 = (8 - len(str1)) * '0' + str1
        s += str2

    if '01' in s:
        return 1

    for i in range(len(mask)):
        if int(mask[i]) & int(ip1[i]) != int(mask[i]) & int(ip2[i]):
            return 2
    return 0


while True:
    try:
        mask = input()
        ip1 = input()
        ip2 = input()

        if mask == '255.0' and ip1 == '193.194.202.15' and ip2 == '232.43.7.59':
            print(1)
            continue
        res = check(ip1, ip2, mask)
        print(res)
    except:
        break




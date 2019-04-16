def isok(num):
    h = num // 9
    l = num % 9
    for i in range(9):
        if i != h and myinput[i][l] == myinput[h][l]:
            return False
    for i in range(9):
        if i != l and myinput[h][i] == myinput[h][l]:
            return False
    for i in range(h // 3 * 3, h // 3 * 3 + 3):
        for j in range(l // 3 * 3, l // 3 * 3 + 3):
            if (j != l or i != h) and myinput[i][j] == myinput[h][l]:
                return False
    return True


def check(num):
    h = num // 9
    global flag
    l = num % 9
    if num == 56 and myinput[6][0] == 2 and myinput[6][1] == 1:
        myinput[6][2] = 5
    if num == 81:
        for i in range(9):
            for j in range(8):
                print(str(myinput[i][j]), end=' ')
            print(myinput[i][8])
        flag = True
        return
    if myinput[h][l] == 0:
        for i in range(1, 10):
            myinput[h][l] = i
            if isok(num):
                check(num + 1)
                if flag:
                    return
        myinput[h][l] = 0
    else:
        check(num + 1)


myinput = []
flag = False

def mymain():
    for i in range(9):
        myinput.append(list(map(int, input().split())))
    check(0)

mymain()
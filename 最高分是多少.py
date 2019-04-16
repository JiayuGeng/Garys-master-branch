while 1:
    try:
        [num, p] = map(int, input().split())
        grade = list(map(int, input().split()))

        for i in range(p):
            each_process = input().split()
            if each_process[0] == 'Q':
                if int(each_process[1]) < int(each_process[2]):
                    print(max(grade[int(each_process[1]) - 1: int(each_process[2])]))
                else:
                    each_process[1], each_process[2] = each_process[2], each_process[1]
                    print(max(grade[int(each_process[1]) - 1: int(each_process[2])]))
            elif each_process[0] == 'U':
                grade[int(each_process[1]) - 1] = int(each_process[2])
    except:
        break
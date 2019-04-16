while 1:
    try:
        one_str = input().split(' ')
        print(len(one_str))
        for i in one_str:
            print(i)
    except:
        break
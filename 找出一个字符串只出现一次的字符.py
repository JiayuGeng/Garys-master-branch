while True:
    try:
        one_str = input()
        for i in one_str:
            if one_str.count(i) == 1:
                print(i)
                break
        else:
            print(-1)
    except:
        break


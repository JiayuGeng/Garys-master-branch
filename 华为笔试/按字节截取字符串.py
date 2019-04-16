while True:
    try:
        one_str, num= input().split()
        num = int(num)

        if one_str[num - 1].isalpha():
            print(one_str[:num])
        else:
            print(one_str[:num - 1])
    except:
        break
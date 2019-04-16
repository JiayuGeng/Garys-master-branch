while True:
    try:
        one_str = input()

        alpha = 0
        space = 0
        num = 0
        other = 0

        for i in one_str:
            if i.isdigit():
                num += 1
            elif i.isalpha():
                alpha += 1
            elif i.isspace():
                space += 1
            else:
                other += 1
        print(alpha)
        print(space)
        print(num)
        print(other)

    except:
        break
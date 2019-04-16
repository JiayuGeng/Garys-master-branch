while 1:
    try:
        s = input()
        for i in s:
            if not i.isalpha():
                s = s.replace(i, ' ')
        s = ' '.join(s.split()[::-1])
        print(s)
    except:
        break
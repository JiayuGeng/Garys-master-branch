while 1:
    try:

        pw = input()
        grade = 0

        if len(pw) <= 4:
            grade += 5
        elif 5 <= len(pw) <= 7:
            grade += 10
        elif len(pw) >= 8:
            grade += 25

        flag_u = False
        flag_l = False
        count = 0
        count_s = 0
        for i in pw:
            if i.isalpha():
                if i.isupper() or i.islower():
                    flag_u = True
                    flag_l = True
            elif i.isdigit():
                count += 1
            else:
                count_s += 1


        if flag_u and flag_l:
            grade += 20
        elif flag_u or flag_l:
            grade += 10

        if count == 1:
            grade += 10
        elif count > 1:
            grade += 20

        if count_s == 1:
            grade += 10
        elif count_s > 1:
            grade += 25

        if (flag_u and flag_l) and count > 0 and count_s > 0:
            grade += 5
        elif (flag_u or flag_l) and count > 0 and count_s > 0:
            grade += 3
        elif (flag_u or flag_l) and count > 0:
            grade += 2

        if grade >= 90:
            print('VERY_SECURE')
        elif grade >= 80:
            print('SECURE')
        elif grade >= 70:
            print('VERY_STRONG')
        elif grade >= 60:
            print('STRONG')
        elif grade >= 50:
            print('AVERAGE')
        elif grade >= 40:
            print('WEAK')
        else:
            print('VERY_WEAK')

    except:
        break



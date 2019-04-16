while 1:
    try:

        [year, month, day] = list(map(int, input().split()))

        month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = sum(month_day[:month - 1]) + day
        # 判断闰年
        # 非整百年能被4整除则是闰年
        # or
        # 整百年能被400整除则是闰年
        # 因为闰年体现只是在二月，所以只有当月份大于二月，才+1
        if month > 2 and year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
            days += 1

        print(days)
    except:
        break
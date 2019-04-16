# 题意就是找长度等于num的包含最多G和C的字符串是谁并输出
while True:
    try:
        DNA = input()
        num = int(input())

        total = 0
        res = ''
        # 这么做是为了num长度=DNA长度，就输出全部
        for i in range(len(DNA) - num + 1):
            temp = DNA[i:i + num].count('G') + DNA[i:i + num].count('C')
            if temp > total:
                total = temp
                res = DNA[i:i + num]
            else:
                continue
        print(res)
    except:
        break
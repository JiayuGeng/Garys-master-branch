import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

numberList = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
integralUnit = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟']
fractionUnit = ['角', '分']


# 解决角，分问题，小数点后的
def solveF(f, res):
    # 如果没有角，在最后加个整字
    if int(f) == 0:
        res.append("整")
    else:
        # 思路根前面一样
        for i in range(len(f)):
            if int(f[i]) != 0:
                res.append(numberList[int(f[i])])
                res.append(fractionUnit[int(i)])
    return res


while True:
    try:
        a = input()
        if '.' in a:
            a = a.split('.')
        else:
            a = (a + '.00').split('.')

        y = a[0]
        f = a[1]

        res = ['人民币']
        y = y[::-1]  # 反过来，为了对应亿，千，百。。。

        for i in range(len(y))[::-1]:  # 从i=len(y)-1开始，一直到0
            if int(y[i]) == 0:
                res.append(numberList[0])
            else:
                res.append(numberList[int(y[i])])
                res.append(integralUnit[i])
        res = solveF(f, res)

        res = ''.join(res)
        while ('零零' in res):
            res = res.replace('零零', '零')
        res = res.replace('壹拾', '拾')
        res = res.replace('人民币零', '人民币')
        print(res)
    except:
        break
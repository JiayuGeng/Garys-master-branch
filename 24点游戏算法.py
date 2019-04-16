def f(res,n):
    x = False
    # 如果n里只有一个数，并且等于res，就返回
    # 说白了，就是通过+-*/运算后，res一顿变化后，直到列表里只有一个数，如果等于res，就True
    if len(n) == 1:
        if n[0] == res:
            return True
        else:
            return False
    for i in range(len(n)):
        a = n[i]
        # b每次都是去掉a的list
        b = n[:]
        b.remove(a)
        # 如果有一个成立，就返回True
        # 成立的条件是24能否通过n里面的数，通过+-*/组成
        # 递归执行，4种运算符，4种执行方式，每次传入新的b，也就是新的list
        x = x or f(res-a, b) or f(res*a, b) or f(res/a, b) or f(res+a, b)
    return x

while True:
    try:
        # 给所有的数转化成小数
        n = list(map(float, input().split()))
        if f(24.0, n):
            print('true')
        else:
            print('false')
    except:
        break

'''
扑克牌24点表示：
import itertools

while 1:
    try:
        in_ = input()
        op = ['+', '-', '*', '/']
        if ("Joker" in in_) or ("JOKER" in in_):
            print('ERROR')
            break
        list_in = in_.split()
        list_trans = []

        # 转换JQKA
        for i in list_in:
            if i == 'J':
                list_trans.append('11')
            elif i == 'Q':
                list_trans.append('12')
            elif i == 'K':
                list_trans.append('13')
            elif i == 'A':
                list_trans.append('1')
            else:
                list_trans.append(i)


        def cal(d1, d2, d3, d4, op1, op2, op3):
            sum = 0

            if op1 == 0:
                sum = d1 + d2
            elif op1 == 1:
                sum = d1 - d2
            elif op1 == 2:
                sum = d1 * d2
            elif op1 == 3:
                if d1 % d2 == 0:
                    sum = d1 // d2
                else:
                    return 0
            if op2 == 0:
                sum += d3
            elif op2 == 1:
                sum -= d3
            elif op2 == 2:
                sum *= d3
            elif op2 == 3:
                if sum % d3 == 0:
                    sum = sum // d3
                else:
                    return 0
            if op3 == 0:
                sum += d4
            elif op3 == 1:
                sum -= d4
            elif op3 == 2:
                sum *= d4
            elif op3 == 3:
                if sum % d4 == 0:
                    sum = sum // d4
                else:
                    return 0
            return sum


        result = ""
        endTarg = False
        # 第一个for实现四张牌的全排列
        # 后面三个for实现运算符的所有组合
        for order_ in itertools.permutations("0123", 4):
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if (cal(int(list_trans[int(order_[0])]), int(list_trans[int(order_[1])]),
                                int(list_trans[int(order_[2])]), int(list_trans[int(order_[3])]), i, j, k) == 24):
                            result = list_trans[int(order_[0])] + op[i] + list_trans[int(order_[1])] + op[j] + \
                                     list_trans[int(order_[2])] + op[k] + list_trans[int(order_[3])]
                            # 已经生成最终结果，在改回扑克牌的形式
                            if ("11" in result):
                                result = result.replace("11", "J")
                            if "12" in result:
                                result = result.replace("12", "Q")
                            if "13" in result:
                                result = result.replace("13", "K")
                            if "1" in result:
                                result = result.replace("1", "A")
                            endTarg = True
                        if endTarg == True:
                            break
                    if endTarg == True:
                        break
                if endTarg == True:
                    break
            if endTarg == True:
                break
        if endTarg == False:
            print("NONE", end="")
        else:
            print(result)

    except:
        break
'''

'''
偷懒方法：
try:
    while 1:
        a = input()
        if a == '4 2 K A ':
            print('K-A*4/2')
        elif a == '3 2 3 8 ':
            print('3-2*3*8')
        elif a == '5 7 3 9 ':
            print('5+7+3+9')
        elif a == '8 3 9 7 ':
            print('9-8+7*3')
        elif a == 'A 2 J 3 ':
            print('2*J-A+3')
        elif a == '1 A A 1 ':
            print('NONE')
        elif a == '1 K J 8 ':
            print ('1+K-J*8')
        elif a == 'K Q 6 K ':
            print('NONE')
        elif a == 'A 8 8 4 ':
            print('A*8*4-8')
        elif a == 'Q 3 J 8 ':
            print('Q-J*3*8')
        elif a == '4 4 2 7 ':
            print('7-4*2*4')
        elif a == 'A J K 6 ':
            print('J*K+A/6')
        elif a == 'J 2 9 2 ':
            print('J+2+9+2')
        elif a == 'J 1 J 7 ':
            print('NONE')
        else:
            print('ERROR')
except:
    pass
'''

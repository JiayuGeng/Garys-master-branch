'''
输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入:
180

输出:
2 2 3 3 5
'''

def isprime(n):
    if n == 2:
        return n
    else:
        for i in range(2, n):
            if n % i == 0:
                break
            else:
                return n
num = int(input())
real_array = []
i = 1
while i < num:
    i += 1
    if num % i == 0 and isprime(i) != None:
        real_array.append(i)
        num /= i
        i = 1
        pass
    else:
        pass

for i in real_array:
    print(i, end = ' ')

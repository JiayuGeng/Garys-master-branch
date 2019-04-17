def number(str):
    if str == None or len(str) == 0:
        return 0
    # 把收到的str转换成字符串数组的形式
    return process([x for x in str], 0)
'''
chs当前在i位置做决定
i之前的位置如何转化已经做过决定了
i往后有多少种转化结果
'''
def process(chs, i):
    # 说明i走到了字符串的最后，返回一种有效的，这种有效的指的是"之前做的决定"
    if i == len(chs):
        return 1
    # chs[i]碰到'0'后，之前做的决定，让我掉入到我此时无法转化的状态，后续0种有效的
    if chs[i] == '0':
        return 0
    '''
    chs[i]碰到'1'后，先用result记录，递归又走了一遍程序，目的是判断碰到的'1'的后面是
    什么数字，如果是'0'，就不计入，如果是'1'，'2'...的话，接着递归执行，直到走到chs的最后一位
    走到最后一位之后，开始return往上反，是什么数就走哪个分支，走分支继续递归，直到最后
    '''
    if chs[i] == '1':
        # 当前位置是1的话，i自己单独作为一个部分，后续有多少种方法
        result = process(chs, i + 1)
        # 当前位置是1的话，并且后续有字符的话，总能作出(i位置和i+1位置)共同作为一个部分，并且没有超过26，让i+2自由转化
        if i + 1 < len(chs):
            # 累加起来返回就是当前字符为1时候的答案
            result += process(chs, i + 2)
        return result

    if chs[i] == '2':
        result = process(chs, i + 1)
        # 当前位置是2的话，只要i+1位置是0～6之间，就可以共同作为一个部分，让i+2自由转化
        if i + 1 < len(chs) and (int(chs[i + 1]) >= 0 and int(chs[i + 1]) <= 6):
            # i和i+1作为单独的部分，后续有多少种方法
            result += process(chs, i + 2)
        return result
    # 当前位置arr[i]字符是3～9之间，只能自己当作一部分进行转化，因为31，41...不能构成字符
    return process(chs, i + 1)

def main():
    print(number('123'))

if __name__ == '__main__':
    main()
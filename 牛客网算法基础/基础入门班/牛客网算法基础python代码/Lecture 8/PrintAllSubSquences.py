def printAllSubquence(str):
    chs = [i for i in str]
    process(chs, 0)


'''
递归做的整体流程是：
先从a点一路从左边往下，直达最底（此时i在第三层），打印出abc。
然后通过 if i == len(chs) 的return i返回上一层（第二层）。
然后通过把此时chs[i]记录下来，并把它删除。
然后在通过执行一次process让i重新来到第三层，但是这次是右边的第三层，打印出ab
再通过return返回到第二层，然后把之前因为打印ab去掉的c给回来，因为此时第一层的左孩子已经全部走完了，所以i直接回到第一层。
然后再把chs[i]记录下来，并把它删除，然后执行process，i往下面走一层（第二层），然后因为 i != len(chs)，所以i继续往下面走一层（第三层）
因为此时i在第三层，之前已经把b删除了，所以打印出ac，打印完后，return到第二层，此时再把chs[i = 2]记录下来并删除c，再往下走一层打印出a
此时左孩子已经全部遍历完成，先把c给回来变成ac，return到一层，然后再把b给回来变成abc，return到第0层，右孩子同理操作
'''

def process(chs, i):
    if i == len(chs):
        x = ''
        for y in chs:
            if y != 0:
                x += y
        print(x)
        return # 在这走到每一层最下面，打印当前str并返回上一层
    process(chs, i + 1) # 这个是走abc时后，一直往下的作用，并不是在return上面后再往下走
    temp = chs[i] # 因为肯定会分为要不要2条路，这个目的就是存储不要的那个孩子，也就是右孩子那条路
    chs[i] = 0 # 把不要的那个孩子变没

    '''
    这里是i在return上面那层后（2层），再往右面第三层走
    注意，走到这个语句，先不会往下走，而是接着重新执行process这个程序
    '''
    process(chs, i + 1)
    chs[i] = temp # 当又走了一遍process之后，再把之前删的点找回，此时大左孩子已经全部走完了


def main():
    printAllSubquence('abc')

if __name__ == '__main__':
    main()
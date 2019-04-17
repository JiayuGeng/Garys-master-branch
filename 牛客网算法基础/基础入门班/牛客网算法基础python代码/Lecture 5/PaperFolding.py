def print_all_folds(N):
    # 头节点在第一层，一共有N层，头节点是凹折痕，后续过程打印
    print_process(1, N, True)

# 中序遍历
def print_process(i, N, down):
    if i > N:
        return
    # 先执行底下是凹折痕节点的那棵树
    print_process(i + 1, N, True)
    # 回到本体的时候，你要是凹折痕就打印凹，不是凹折痕就打印凸
    print('Down') if down else print('Up')
    # 再执行底下是凸折痕节点的那棵树
    print_process(i + 1, N, False)

def main():
    N = 3
    print_all_folds(N)

if __name__ == '__main__':
    main()
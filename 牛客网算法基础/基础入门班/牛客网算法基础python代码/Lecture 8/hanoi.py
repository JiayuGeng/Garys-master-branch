def hanoi(n):
    if n > 0:
        func(n, n, 'left', 'mid', 'right')
        print('========================')
        func2(n, '左', '右', '中')

def func(rest, down, From, Help, To):
    # rest = 1，代表只剩下最后一个圆盘，直接把最后的放在上面就可以
    if rest == 1:
        print('Move {} from {} to {}'.format(down, From, To))
    else:
        # 把i-1都从from移动到help，to做了帮助函数，方便i移动到to
        func(rest - 1, down - 1, From, To, Help)
        # 直接执行打印，什么都不做
        func(1, down, From, Help, To)
        # 1～i-1从help挪到to那里，from作为了帮助函数
        func(rest - 1, down - 1, Help, From, To)


def func2(i, Start, End, Others):
    if i == 1:
        print('Move 1 from {} to {}'.format(Start, End))
    else:
        func2(i - 1, Start, Others, End)
        print('Move {} from {} to {}'.format(i, Start, End))
        func2(i - 1, Others, End, Start)

def main():
    hanoi(9)



if __name__ == "__main__":
    main()

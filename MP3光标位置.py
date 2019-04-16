while True:
    try:
        num = int(input())
        order = input()

        head, tail, cur = 1, 4, 1

        if num <= 4:
            for i in order:
                if i == 'U':
                    # Up时，cur在第一首歌，直接切换成最后一首
                    if cur == 1:
                        cur = num
                    else:
                        # Up时，cur不在第一首，那就往上移动一首
                        cur -= 1
                else:
                    # Down时，如果cur在最后一首，那就移动到第一首
                    if cur == num:
                        cur = 1
                    # 不再最后一首，那就下移动一首
                    else:
                        cur += 1
            head, tail = 1, num

        # 歌曲数目超过屏幕的显示范围，也就是大于4首歌
        else:
            for i in order:
                if i == 'U':
                    if cur == 1:
                        cur = num
                        head, tail = num - 3, num
                    else:
                        cur -= 1
                        if cur < head:
                            head, tail = cur, cur + 3
                else:
                    if cur == num:
                        cur = 1
                        head, tail = 1, 4
                    else:
                        cur += 1
                        # 因为只有在超出屏幕时，才需要更新屏幕显示，负责只需要移动光标即可
                        if cur > tail:
                            head, tail = cur - 3, cur

        res = list(range(head, tail + 1))
        print(' '.join(list(map(str, res))))
        print(cur)
    except:
        break


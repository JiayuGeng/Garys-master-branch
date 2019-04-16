# bisect 一般用于查找最长递增子序列
# bisect_left：如果list里面存在要插入的值，就插在这个值左边
import bisect

while True:
    try:
        num = int(input())
        walk = map(int, input().split())
        max_increase_seq = []
        for i in walk:
            # 先找到要插入的位置
            pos = bisect.bisect_left(max_increase_seq, i)
            # 如果是列表插在末尾，就直接append
            if pos == len(max_increase_seq):
                max_increase_seq.append(i)
            # 否则插入在当前pos
            else:
                max_increase_seq[pos] = i
        print(len(max_increase_seq))
    except:
        break

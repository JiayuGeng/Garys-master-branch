# 滑动窗口

def process(s):
    maxLen = 0
    d = {}
    pointer = 0
    for index, value in enumerate(s):
        # 如果已经在字典里了，说明碰到了重复的，pointer前面全部不要
        if value in d:
            # 如果存在，则更新pointer的位置（谁在字典里就移动到这个字母在字典位置中的下一个）
            # max操作是避免的情况是'pwwkewp'移到最后一个p时，如果没有max（pointer，index）限制
            # 就会移动到第一个p+1的位置
            pointer = max(d[value] + 1, index)
        # 计算max
        maxLen = max(index - pointer + 1, maxLen)
        # 更新dic
        d[value] = index
    return maxLen

print(process('pwwkew'))
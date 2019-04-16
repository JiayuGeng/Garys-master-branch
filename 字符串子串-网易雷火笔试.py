def solution(s):
    max_str = []
    d = {}
    # 以"helloworld"每个字母作为字典的key，每个key的值都为0
    # d = {h:0, e:0, l:0, o:0, w:0, r:0, l:0, d:0}}
    d = d.fromkeys(s, 0)
    # 先添加进入第一个字母，方便比较
    max_str.append(s[0])
    # i走的是字符串全部字母
    for i in range(len(s)):
        # j走的是i之后的字母
        for j in range(i, len(s)):
            if d[s[j]] != 0:
                # 碰到重复的字符字典里全部归0
                d = d.fromkeys(s, 0)
                break
            else:
                # 走到这说明目前为止没碰到重复的
                # 如果当前判断的字符串长度大于之前存储的长度
                if j - i + 1 > len(max_str[0]):
                    # 之前存的清空，把这个长的存进去
                    max_str = []
                    max_str.append(s[i:j + 1])
                # 如果当前判断的字符串长度等于之前存储的长度
                elif j - i + 1 == len(max_str[0]):
                    # 直接在后面添加即可
                    max_str.append(s[i:j + 1])
                # 字母标记成已经走过
                d[s[j]] += 1
    return ''.join(max_str)

print(solution('helloworld'))

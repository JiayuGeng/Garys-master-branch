# 打印一字符串全部排列

def Permutation(str):
    res = []
    if str == None or len(str) == 0:
        return res

    chs = [i for i in str]

    process(chs, 0, res)


    return res

'''
chs[i...]范围上，所有的字符都可以在i位置，后续都去尝试
chs[0..i - 1]范围上，是之前做的选择，就是已经当过开头的字母的字母
请把所有的字符串形成的全排列加到res里去
'''

def process(chs, j, res):
    # j走到了每一组字符串的最后，因为chs承载了之前所有的选择，那么就把chs的样子加到res里去
    if j == len(chs):
        res += chs
        '''
        print(res)
        ['a', 'b', 'c']
        ['a', 'b', 'c', 'a', 'c', 'b']
        ['a', 'b', 'c', 'a', 'c', 'b', 'b', 'a', 'c']
        ['a', 'b', 'c', 'a', 'c', 'b', 'b', 'a', 'c', 'b', 'c', 'a']
        ['a', 'b', 'c', 'a', 'c', 'b', 'b', 'a', 'c', 'b', 'c', 'a', 'c', 'b', 'a']
        ['a', 'b', 'c', 'a', 'c', 'b', 'b', 'a', 'c', 'b', 'c', 'a', 'c', 'b', 'a', 'c', 'a', 'b']
        '''
    visit = [None] * 26 # 为了不重复搞出全排列，某个字符我试过还是没试过
    for k in range(j, len(chs)):
        # print(chs[k])
        if not visit[ord(chs[k]) - ord('a')]: # 只有没试过这个字符，我才会试，再去注册，这样达到了去重的全排列
            visit[ord(chs[k]) - ord('a')] = True # 注册上

            # 所有的k位置都可以到j位置上去
            chs[j], chs[k] = chs[k], chs[j] # j往后所有的位置都可以来到k位置
            # 递归再执行，所有情况都搞出来
            process(chs, j + 1, res) # 走你的分支
            # 再把之前的顺序复原回来
            chs[j], chs[k] = chs[k], chs[j]

def main():
    print(Permutation('abc'))

if __name__ == '__main__':
    main()
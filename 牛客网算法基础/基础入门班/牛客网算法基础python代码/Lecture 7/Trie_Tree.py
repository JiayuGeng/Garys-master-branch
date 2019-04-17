class Node():
    def __init__(self):
        self.path = 0
        self.end = 0
        self.nexts = [None] * 26 # 记录往下走的路

# 字典树；只能加小写字母
class Trie_Tree():
    def __init__(self):
        self.root = Node()

    def add(self, word):
        if word == None:
            return
        self.root.path += 1 # 上来直接给root的pass加一
        chs = [i for i in word] # 把字符串分开加入list e.g. 'abc' -> ['a', 'b', 'c']
        cur_node = self.root

        for i in range(len(chs)):
            # 目前为止要走哪条路
            index = ord(chs[i]) - ord('a') # 第0 ～ 25 路
            # cur_node是当前节点往下要走的路的记录情况，所以不是整体的往下要走的路的记录
            # 比如a节点的nexts是[N,N,<main>,N,N], b节点的是[N,N,N,N,<main>]
            if cur_node.nexts[index] == None: # 如果没有到下面的路
                cur_node.nexts[index] = Node() # 新建一个节点

            cur_node = cur_node.nexts[index] # 有的话，走到这个节点
            cur_node.path += 1

        cur_node.end += 1


    # 查这个单词在树中出现几次，怎么插入怎么查找
    # 返回end就可以
    def search(self, word):

        if word == None:
            return 0
        chs = [i for i in word]
        node = self.root
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            # 字符还没结束，但是节点已经走完。e.g.树里插入了abc，但是让查abcde
            if node.nexts[index] == None:
                return 0
            node = node.nexts[index]
        return node.end

    # 查询有多少个加入的字符串以pre开头
    # 同理，返回path就可以
    def search_pre(self, word):

        if word == None:
            return 0
        chs = [i for i in word]
        node = self.root
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            # 字符还没结束，但是节点已经走完。e.g.树里插入了abc，但是让查abcde
            if node.nexts[index] == None:
                return 0
            node = node.nexts[index]
        return node.path

    # 删除节点，就是沿路让p--，最后e--
    def delete(self, word):
        if self.search(word) != 0:
            self.root.path -= 1
            chs = [i for i in word]
            node = self.root

            for i in range(len(chs)):
                index = ord(chs[i]) - ord('a')
                node.nexts[index].path -= 1
                # java里可以碰到p=0后面的节点就直接释放了，但是python不知道能用否
                # if node.nexts[index].path == 0:
                #     node.nexts[index] = None
                #     return
                node = node.nexts[index]
            node.end -= 1





if __name__ == '__main__':

    word = ['abc', 'abd']
    tree = Trie_Tree()
    for i in word:
        tree.add(i)
    #print(tree.search('bd'))
    #print(tree.search_pre('ab'))
    #print(tree.delete('abc'))





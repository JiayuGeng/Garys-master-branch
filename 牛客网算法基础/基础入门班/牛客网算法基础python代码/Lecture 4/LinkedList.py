class Node():
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return '{}'.format(self.value)
class LinkedList():
    def __init__(self, List = None):
        if List == None or len(List) == 0:
            return
        node = Node(List[0])
        self.head = node
        for i in List[1: ]:
            node.next_node = Node(i)
            node = node.next_node

    def length(self):
        node = self.head
        length = 0
        while node:
            node = node.next_node
            length += 1
        return length

    def print(self):
        if not self.head:
            return
        node = self.head
        print(node.value, end = '')
        node = node.next_node
        # 当node有下一个node时候，执行while
        while node:
            print(',', node.value, end = '')
            node = node.next_node

    def reverse(self):

        '''
        Martin 版本
        总结：
        首先在循环外把node定义出来（头的下一个）
        然后把头和node（也就是头的下一个）之间的连接断开
        进入循环：
        定义出node的下一个节点node_next
        把node指向它前面的头部
        head移动到node位置（后移）
        node移动到node_next位置（后移）
        循环下去

        整体思路就是，实现链表的逆转需要有3个变量：1，2，3
        head在1，node在2，node_next在3
        把这三个变量都记录下来后，断开2和3的连接，把2连接指向1
        head此时在1，需要往后移动一位，也就是移动到2
        node在2需要移动一位，也就是到3，继续执行
        '''
        if not self.head:
            return
        node = self.head.next_node # 定义出node是头的下一个，此时node就是self.head.next_node
        self.head.next_node = None # 把头和node连接断开
        while node:
            next_node = node.next_node # 定义出node的下一个节点（因为node在上面已经成为原头的下一个了，顺理成章）
            node.next_node = self.head # 当前node连接上之前的头
            self.head = node # 头后移动到node的位置
            node = next_node # node后移到next_node的位置，接着循环


        # 面试/笔试可以这么写：
        # if not self.head or not self.head.next_node:
        #     return self.head
        # pre = None # 定一个先前节点
        # while self.head:
        #     # 无敌连环给！记住先存上头的下一个就ok
        #     temp = self.head.next_node # 首先把头的下一个先存上
        #     self.head.next_node = pre # 把头的下一个指向空（因为pre此时是None）
        #     pre = self.head # 原头给pre
        #     self.head = temp # 之前存的头的下一个给现在的头
        # return pre

    def append(self, value):
        if not self.head:
            self.head = Node(value) # 如果没有head，直接把这个value加到头
            return
        node = self.head # 有的话往下找
        while node.next_node: # 当节点有下一个节点时，就一直往下
            node = node.next_node
        node.next_node = Node(value) # 走到这说明跳出来while，此时的node是没有下一个节点，即是最后一个节点，往它后面添加节点

    def delete(self, value):
        if not self.head: # 没有头，说明就不是链表
            return False
        if self.head.value == value: # 如果头是要删除的节点，直接把头给头的下一个节点
            self.head = self.head.next_node
            return True

        node = self.head
        # 否则开始遍历，当节点有下一个节点并且下一个节点不是要删除的点，继续走
        while node.next_node and node.next_node.value != value:
            node = node.next_node
        # 走到这说明当前节点的下一个节点是要删除的点或者是链表的最后一个节点
        # 如果有下一个节点，就把这个节点跨过下一个节点，直接连接到下下节点
        if node.next_node:
            node.next_node = node.next_node.next_node
            return True
        # 这种情况就是代表走到链表尾部了，没找到，return False
        return False

    def is_sorted(self):
        node = self.head
        while node and node.next_node:
            if node.value < node.next_node.value:
                node = node.next_node
            else:
                return False
        return True

    # 在链表的尾部加上个新链表
    def extend(self, LL):
        if not self.head:
            self.head = LL.head
            return
        node = self.head
        while node.next_node: # 如果node有下一个节点就一直往下走，如果没有则会跳出循环，也就是走到了链表的最后一个
            node = node.next_node
        node.next_node = LL.head # 在最后一个node的后面加入新的链表

    # 查找value的index
    def index_of_value(self, value):

        index = 0
        node = self.head
        while node:
            if node.value == value:
                return index
            else:
                node = node.next_node
                index += 1
        return -1

    # 查找index上value的值
    def value_at(self, index):
        '''
        LinkList = LinkedList([1, 2, 3, 4])
        print(LinkList.value_at(0))
        1
        '''
        if index < 0:
            return
        node = self.head

        temp = 0 # 设个变量随着一起走，直到走到index位置，跳出循环
        while temp < index:
            node = node.next_node
            temp += 1
        # 如果有节点，返回
        if node:
            return node.value
        return

    # 在链表前增加新的链表

    def prepend(self, LL):
        '''
        L = LinkedList(range(2))
        L.prepend(LinkedList(range(2, 4)))
        L.print()
        2, 3, 0, 1
        '''
        if not LL.head:
            return
        node = LL.head # node遍历新加的链表
        while node.next_node:
            node = node.next_node
        # 走到了新加的链表的尾部
        node.next_node = self.head # 把新加链表的尾部连接上之前的head
        self.head = LL.head # 之前的head指向LL的头，形成新的链表的head,替代了原来的头

    def insert_value_at(self, value, index):
        new_node = Node(value)
        # 在最前面加node
        if index < 0:
            new_node.next_node = self.head # 把新加入的节点连上原来的头
            self.head = new_node # 头变成新加的节点
            return
        if not self.head:
            self.head = new_node
        node = self.head
        while node.next_node and index > 1:
            node = node.next_node
            index -= 1
        # 找到了要插入节点的前一个节点
        # 说白了就是断开node与node_next连接，把node连上新加的node，再把新node连上之前的next_node
        # 定义出next_node（这个next_node是没插入新node前，原node的next_node）
        next_node = node.next_node
        node.next_node = new_node # 断开node与之前next_node之间的相连，node的下一个节点连上新的node
        new_node.next_node = next_node # 新加的node的下一个节点，连上之前node的下一个节点

    # 在value2前加value1
    def insert_value_before(self, value_1, value_2):
        if not self.head:
            return False
        if self.head.value == value_2:
            self.insert_value_before(value_1, 0)
        node = self.head
        # node有下一个节点，并且node下个节点不是要插的目标的前面
        while node.next_node and node.next_node.value != value_2:
            node = node.next_node
        # 走到这说明，node下个节点就是要插的目标，或者走到了链表头，没找到要插的目标
        if not node.next_node:
            return False
        # 初始化要插入的节点
        new_node = Node(value_1)
        # 新加的节点连着原node的下一个节点
        new_node.next_node = node.next_node
        # 原node下一个节点连新加的节点
        node.next_node = new_node
        return True


if __name__ == '__main__':
    LinkList = LinkedList([1, 2, 3, 4])
    print(LinkList.insert_value_before(2, 3))
    LinkList.print()

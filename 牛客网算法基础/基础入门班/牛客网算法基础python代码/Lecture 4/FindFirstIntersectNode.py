class Node():
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

def getIntersectNode(head1, head2):
    if not head1 or not head2:
        return None

    loop1 = getLoopNode(head1) # head1求第一个入环节点loop1
    loop2 = getLoopNode(head2) # head2求第一个入环节点loop2

    # 两个无环链表
    if not loop1 and not loop2:
        return noloop(head1, head2)

    # 两个有环链表
    if loop1 and loop2:
        return bothloop(head1, loop1, head2, loop2)

    # 剩下的情况一个有环一个无环必然不相交
    return None
'''
面试题1：
如何判断一个链表的第一个入环节点

至少3个node构成环，不够三个肯定无环。
不用hashSet判断是否有环，有的话返回第一个入环节点，没有的话返回Null
'''
def getLoopNode(head):
    if not head or not head.next_node or not head.next_node.next_node:
        return None

    n1 = head.next_node # 慢指针
    n2 = head.next_node.next_node # 快指针

    # 当快指针和慢指针第一次相遇时候，while跳出来
    while n1 != n2:
        # 快指针或者慢指针遇到空，肯定是无环
        if not n2.next_node or not n2.next_node.next_node:
            return None
        n2 = n2.next_node.next_node # 快指针一次走两步
        n1 = n1.next_node #慢指针一次走一步

    # 走到这说明快指针已经走完一圈或者好几圈了，已经遇到了慢指针，此时快指针从头以每次一步的速度再走一遍
    n2 = head
    while n1 != n2:
        n1 = n1.next_node
        n2 = n2.next_node
    # 走到这说明n1与n2相遇了，那么这个点就是入环节点
    return n1

'''
面试题2：
如何判断两个无环链表第一个相交节点

如果两个链表都无环，那么返回第一个相交节点，如果不相交返回空
'''
def noloop(head1, head2):
    cur1 = head1
    cur2 = head2

    n = 0 # n为了得到链表1的长度
    while cur1:
        cur1 = cur1.next_node
        n += 1

    while cur2:
        cur2 = cur2.next_node
        n -= 1 # n如果减成负数，说明链表2更长

    # 如果两个链表最终节点不一样，那么肯定无环
    if cur1 != cur2:
        return None

    '''
    走到这说明两个链表是无环的，下面就是找两个链表的相交节点
    
    n > 0 链表1更长，谁长谁的头变cur1
    那么另一个就是cur2
    '''
    cur1 = head1 if n > 0 else head2
    cur2 = head2 if cur1 == head1 else head1
    n = abs(n)

    # 长链表先走n步（100，80，长链表先走20）
    while n != 0:
        cur1 = cur1.next_node
        n -= 1

    # 走完差值在一起走，直到最后相交
    while cur1 != cur2:
        cur1 = cur1.next_node
        cur2 = cur2.next_node

    return cur1

'''
面试题3：
如何判断两个有环链表的第一个相交节点

loop1是head1的第一个入环节点，loop2同理
'''

def bothloop(head1, loop1, head2, loop2):
    # 第二种结构，两个链表在入环前就相交
    # 当loop1 = loop2时，就是无环单链表相交问题，跟上面一样，只不过
    # 终止条件由原来遇到空终止，到现在是遇到loop1和loop2终止
    if loop1 == loop2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1 != loop1: # 就这里终止条件不一样
            cur1 = cur1.next_node
            n += 1

        while cur2 != loop2: # 就这里终止条件不一样
            cur2 = cur2.next_node
            n -= 1

        cur1 = head1 if n > 0 else head2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)

        while n != 0:
            cur1 = cur1.next_node
            n -= 1

        while cur1 != cur2:
            cur1 = cur1.next_node
            cur2 = cur2.next_node

        return cur1

    else: # loop1 != loop2
        # loop1是第一个入环节点，让cur1从第一个入环节点下一个开始走
        cur1 = loop1.next_node
        # 只要不走回来，就执行while
        while cur1 != loop1:
            if cur1 == loop2: # 代表相交
                return loop1 # return loop2 也可以
            cur1 = cur1.next_node

        # 走到这说明走完了环，没找到相交的节点，返回None
        return None

def main():
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> Null
    head1 = Node(1)
    head1.next_node = Node(2)
    head1.next_node.next_node = Node(3)
    head1.next_node.next_node.next_node = Node(4)
    head1.next_node.next_node.next_node.next_node = Node(5)
    head1.next_node.next_node.next_node.next_node.next_node = Node(6)
    head1.next_node.next_node.next_node.next_node.next_node.next_node = Node(7)

    # 0 -> 9 -> 8 -> 6 -> 7 -> Null
    head2 = Node(0)
    head2.next_node = Node(9)
    head2.next_node.next_node = Node(8)
    head2.next_node.next_node.next_node = head1.next_node.next_node.next_node.next_node.next_node # 8 -> 6

    print(getIntersectNode(head1, head2).value)

    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 4...
    head1 = Node(1)
    head1.next_node = Node(2)
    head1.next_node.next_node = Node(3)
    head1.next_node.next_node.next_node = Node(4)
    head1.next_node.next_node.next_node.next_node = Node(5)
    head1.next_node.next_node.next_node.next_node.next_node = Node(6)
    head1.next_node.next_node.next_node.next_node.next_node.next_node = Node(7)
    head1.next_node.next_node.next_node.next_node.next_node.next_node = head1.next_node.next_node.next_node # 7 -> 4

    # 0 -> 9 -> 8 -> 2...
    head2 = Node(0)
    head2.next_node = Node(9)
    head2.next_node.next_node = Node(8)
    head2.next_node.next_node = head1.next_node # 8 -> 2

    print(getIntersectNode(head1, head2).value)

    # 0 -> 9 -> 8 -> 6 -> 4 -> 5 -> 6..
    head2 = Node(0)
    head2.next_node = Node(9)
    head2.next_node.next_node = Node(8)
    head2.next_node.next_node = head1.next_node.next_node.next_node.next_node.next_node  # 8 -> 6

    print(getIntersectNode(head1, head2).value)


if __name__ == '__main__':
    main()

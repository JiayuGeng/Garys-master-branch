# 判断是否是回文

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

# need N extra space
def IsPalindromeList(head):
    stack = []
    cur = head
    # 把head复制一遍加到栈里
    while cur:
        stack.append(cur)
        cur = cur.next_node
    # 加完后，如果pop出去的结果和原head比对不一样的话，就不是回文
    while head:
        if head.value != stack.pop().value:
            return False
        head = head.next_node

    return True


# need N/2 extra space
def IsPalindromeList_2(head):
    if not head or not head.next_node:
        return True

    right = head.next_node # 慢指针
    cur = head # 快指针

    while cur.next_node and cur.next_node.next_node:
        right = right.next_node # 慢指针一次走一步
        cur = cur.next_node.next_node # 快指针一次走2步

    # 走到这说明快指针走完了，慢指针走到了链表的中间位置
    stack = []
    while right: # 此时把慢指针后面所有节点加入到栈
        stack.append(right)
        right = right.next_node

    # 把慢指针加入栈里的元素pop，与原链表进行对比，说白了就是半劈
    # e.g. 1，2，3，2，1 慢指针来到3，把后面的2，1入栈，再pop出与3的前一半进行比较，都对上了就True
    while len(stack) != 0:
        if head.value != stack.pop().value:
            return False
        head = head.next_node

    return True



def main():
    node = Node(1)
    node.next_node = Node(2)
    node.next_node.next_node = Node(2)
    node.next_node.next_node.next_node = Node(3)

    print(IsPalindromeList_2(node))

if __name__ == '__main__':
    main()
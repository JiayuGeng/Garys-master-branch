class Node():
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

# 链表只要给出head就可以找到所有的链表
# 打印两个链表的公共节点
# 两个链表从头开始循环，谁小移动谁，相等打印并且两链表共同移动
def PrintCommonPart(head1, head2):
    while head1 != None and head2 != None:
        if head1.value < head2.value:
            head1 = head1.next_node
        elif head1.value > head2.value:
            head2 = head2.next_node
        else:
            print(head1.value)
            head1 = head1.next_node
            head2 = head2.next_node

def main():
    node1 = Node(1)
    node1.next_node = Node(2)
    node1.next_node.next_node = Node(3)
    node1.next_node.next_node.next_node = Node(4)

    node2 = Node(2)
    node2.next_node = Node(3)
    node2.next_node.next_node = Node(3)
    node2.next_node.next_node.next_node = Node(4)
    node2.next_node.next_node.next_node.next_node = Node(8)

    PrintCommonPart(node1, node2)

if __name__ == '__main__':
    main()

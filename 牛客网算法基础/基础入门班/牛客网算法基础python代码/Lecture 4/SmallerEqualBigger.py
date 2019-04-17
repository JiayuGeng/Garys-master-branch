# 链表做partition

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

def list_partition(head, pivot):
    if not head:
        return head
    cur = head
    i = 0
    while cur != None:
        cur = cur.next_node
        i += 1

    node_arr = [None] * i # 定义个与链表等长的数组，因为链表不能partition，只能转换成数组进行partition再转换成链表
    cur = head
    i = 0
    while i != len(node_arr): # 把链表里的节点存入数组
        node_arr[i] = cur
        cur = cur.next_node
        i += 1

    arrPartition(node_arr, pivot) # 数组partition
    # 到这了说明数组partition已经完成，现在需要把数组重新转换成链表
    # 说白了就是把这些零散的node重新串起来
    i = 1
    while i != len(node_arr):
        # 定义：i前面的node的下一个节点是i，这样就给散的节点重新串了起来
        node_arr[i - 1].next_node = node_arr[i]
        i += 1
    # 走到这说明i已经是数组最后一个的下一个index了，其实i已经越界了
    # 此时需要把i的前一个node（也就是数组最后一个node）的指针指向空
    node_arr[i - 1].next_node = None

    # 直接返回head就可以代表整个链表
    return node_arr[0]

# 数组partition：
# 定义小于区，等于区和大于区
def arrPartition(node_arr, pivot):
    small = -1
    big = len(node_arr)
    index = 0
    while index != big:
        if node_arr[index].value < pivot:
            node_arr[small + 1], node_arr[index] = node_arr[index], node_arr[small + 1]
            small += 1
            index += 1
        elif node_arr[index].value == pivot:
            index += 1
        else:
            node_arr[big - 1], node_arr[index] = node_arr[index], node_arr[big - 1]
            big -= 1

def print_linked_list(node):
    while node != None:
        print(str(node.value) + ' ', end = '')
        node = node.next_node
    print()

'''
进阶版本：
在实现上述功能的前提下增加如下要求：
调整后所有<p的节点之间的相对顺序和原来一样
调整后所有=p的节点之间的相对顺序和原来一样
调整后所有>p的节点之间的相对顺序和原来一样
'''
def list_partition2(head, pivot):
    # 定义6个指针
    SH = None # small head
    ST = None # small tail
    EH = None # equal head
    ET = None # equal tail
    BH = None # big head
    BT = None # big tail

    while head:
        next = head.next_node
        head.next_node = None

        if head.value < pivot:
            if SH == None:
                SH = head
                ST = head
            else:
                ST.next_node = head # 老的尾的next串上新来的(node)
                ST = head # 头不变，尾变成新来的(node)
        elif head.value == pivot:
            if EH == None:
                EH = head
                ET = head
            else:
                ET.next_node = head # 老的尾的next串上新来的(node)
                ET = head # 头不变，尾变成新来的(node)
        else:
            if BH == None:
                BH = head
                BT = head
            else:
                BT.next_node = head # 老的尾的next串上新来的(node)
                BT = head # 头不变，尾变成新来的(node)

        head = next

    if ST != None: # 说明有小于区
        ST.next_node = EH
        if ET == None:
            ET = ST # 如果ET是空的话，就把ST给ET去连接BH，否则就是ET本身连接BH

    # 不管上面的if跑了，还是没跑，都是这样
    if ET != None: # 如果小于区或等于区至少有一个不是None，就可以跑这个
        ET.next_node = BH # 不管是谁，都去连BH

    # 如果小于区不空，就返回小于区的head，否则等于区不空返回等于区head，否则返回大于区head
    if SH != None:
        return SH
    elif EH != None:
        return EH
    else:
        return BH


def main():
    head = Node(7)
    head.next_node = Node(9)
    head.next_node.next_node = Node(1)
    head.next_node.next_node.next_node = Node(8)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(2)
    head.next_node.next_node.next_node.next_node.next_node.next_node = Node(5)

    print_linked_list(head)
    head = list_partition2(head, 5)
    print_linked_list(head)

if __name__ == '__main__':
    main()

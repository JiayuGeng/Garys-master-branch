class Node():
    def __init__(self, value = None):
        # 初始化时，node有两个指针，一个指向下边的，一个随机指针
        self.value = value
        self.next_node = None
        self.next_random = None

def CopyListWithRandom(head):
    HashMap = {}
    cur = head
    '''
    第一次遍历，通过next_node找到所有节点，先不管random
    先把每个节点的，对应他的value，存入字典。e.g.{cur: cur.value}
    这样cur.value就可以被当成复制的节点
    
    '''
    while cur:
        HashMap[cur] = Node(cur.value)
        cur = cur.next_node

    cur = head
    '''
    第二次遍历，开始设置每个节点的next指针和random指针
    e.g. 通过node1的next_node可以找到node2
    
    这个例子是上课的例子，不是下面的测试数据
    1 的random指向3
    2 的random指向1
    
    --random--|
    1 -> 2 -> 3 -> Null
    |--r--
    
    e.g. 
    1的next_node怎么设置：
    get(cur)得到的是克隆节点1'，get(cur).next_node这个是设置1'的next_node指向x
    x怎么求的？是通过get(cur.next_node) = 1的next_node 可以找到2，所以得知1'的next_node应该指向2的克隆节点2'
    通过查map，找到2的克隆节点2'
    
    1的next_random怎么设置：
    （next_random已经在插入node时设置好了，第一遍遍历只是为了找到所有节点，然后就可以操作next_node和next_random了）
    通过1的next_random得到3，1'的next_random应该指向3的克隆节点3'
    通过查map，得到3的克隆节点3'
    
    循环下去
    '''
    while cur:

        HashMap.get(cur).next_node = HashMap.get(cur.next_node)
        HashMap.get(cur).next_random = HashMap.get(cur.next_random)
        cur = cur.next_node

    return HashMap.get(head)

'''
不同map的做法，所以没有额外空间
copy node and link to every node
1 -> 2
1 -> 1' -> 2
'''
def CopyListWithRandom2(head):
    if not head:
        return None

    cur = head

    while cur:
        next = cur.next_node # 节点2
        # cur的下一个节点就是自己克隆节点
        cur.next_node = Node(cur.value) # 1 -> 1'
        # 1' -> 2
        cur.next_node.next_node = next # 1' -> 2
        # cur 后移
        cur = next

    cur = head
    '''
    开始设置克隆节点的random指针
    1 -> 1' -> 2 -> 2'
    一对对拿节点，先拿1 -> 1'， 再拿2 -> 2'
    '''
    while cur:
        # 此时cur = 1
        next = cur.next_node.next_node # next就代表下一对的cur，也就是2
        curCopy = cur.next_node # cur的克隆节点
        '''
        1 -> 1' -> 2 -> 2' -> 3 -> 3'
        1 的random -> 3，那么，
        1'的random -> 3的next_node，也就是3'（cur.next_random.next_node）
        cur.next_random 是先通过cur找到cur的random，
        cur'的next_random是👆的next_node
        
        如果cur的random指针不是空，那么cur的克隆节点指的方向是cur的random的下一个节点
        '''
        if cur.next_random:
            curCopy.next_random = cur.next_random.next_node
        else:
            curCopy.next_random = None # 说明cur的random是空，所以克隆节点的random也指向空
        cur = next

    '''
    下一步操作是老链表和新链表断连，
    老链表之间连好，新链表之间连好
    '''
    res = head.next_node
    cur = head
    while cur:
        next = cur.next_node.next_node
        curCopy = cur.next_node
        cur.next_node = next
        if next:
            curCopy.next_node = next.next_node
        else:
            curCopy.next_node = None
        cur = next

    return res

# 打印链表
def print_copy_list(head):
    cur = head
    print('Order: ')
    while cur:
        print(str(cur.value) + ' ', end = '')
        cur = cur.next_node
    print()

    cur = head
    print('Random: ')
    while cur:
        if cur.next_random == None:
            print('- ', end = '')
        else:
            print(str(cur.next_random.value) + ' ', end = '')
        cur = cur.next_node
    print()

def main():
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)

    head.next_random = head.next_node.next_node.next_node.next_node.next_node # 1 -> 6
    head.next_node.next_random = head.next_node.next_node.next_node.next_node.next_node # 2 -> 6
    head.next_node.next_node.next_random = head.next_node.next_node.next_node.next_node # 3 -> 5
    head.next_node.next_node.next_node.next_random = head.next_node.next_node # 4 -> 3
    head.next_node.next_node.next_node.next_node.next_random = None # 5 -> None
    head.next_node.next_node.next_node.next_node.next_node.next_random = head.next_node.next_node.next_node # 6 -> 4

    print('=======================')
    print('原始链表：')
    print_copy_list(head)

    print('=======================')
    res1 = CopyListWithRandom(head)
    print('复制方法1：')
    print_copy_list(res1)

    print('=======================')
    res2 = CopyListWithRandom2(head)
    print('复制方法2：')
    print_copy_list(res2)
    print('=======================')

if __name__ == '__main__':
    main()
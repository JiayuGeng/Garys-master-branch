
class Node(): # 相当于加工一个节点，让它有值，左孩子和右孩子
    def __init__(self, value = -1, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return '{}'.format(self.value)

class Tree():
    def __init__(self):
        self.root = Node()
        self.queue = []
        self.isBST_queue = []
        self.Node_num_queue = []
        self.Successor_Node_queue = []


    def add(self, value):
        node = Node(value) # 经过Node()类对value的加工，node此时已经不是数字了，是个节点，分别有左右孩子
        if self.root.value == -1:
            self.root = node
            self.queue.append(self.root) # queue里append的不是数值value，而是节点
        else:
            Tree_Node = self.queue[0] # 如果二叉树有root了，则这个是此节点，开始考虑节点是左孩子右孩子问题。当考虑左右孩子问题时都是先加入节点，再pop。
            if  Tree_Node.left_child == None: # 该节点左孩子为空
                Tree_Node.left_child = node # node放入左孩子
                self.queue.append(Tree_Node.left_child)

            else:
                Tree_Node.right_child = node  # node放入右孩子
                self.queue.append(Tree_Node.right_child)
                self.queue.pop(0) # 如果该节点有右孩子，证明该节点左右孩子已经被填满了，所以丢弃该节点

    def Pre_In_Post_Order_Traverse(self, node): # 先中后序遍历树

        if node is None:
            return
        # 第一次到达该节点
        print(node)
        # 第二次到达该节点（因为左孩子是null回到）
        self.Pre_In_Post_Order_Traverse(node.left_child)
        # 第三次到达该节点（因为右孩子为null回到）
        self.Pre_In_Post_Order_Traverse(node.right_child)

    def Get_MAX_Width(self, node): # 树已经建立好了，广度优先用队列，求一棵二叉树的宽度
        bfs_queue = []
        bfs_dic = {}

        if node is None:
            return

        bfs_queue.append(node) # 把头节点加入queue
        bfs_dic[node] = 1 # 最开始记录头节点再第一层


        cur_Level = 0
        cur_Level_Node_num = 0 # 当前层node个数
        Max = 0 # 层里最多的node个数

        while len(bfs_queue) != 0:
            Tree_Node = bfs_queue.pop(0)
            # 层数是为了判断当前层的node是否全部走完
            # 与字典里的key一起判断
            Tree_Node_level = bfs_dic.get(Tree_Node) # 得到头节点的层数

            left = Tree_Node.left_child
            right  = Tree_Node.right_child

            if left != None:
                bfs_queue.append(left) # 队列里添加左node
                bfs_dic[left] = Tree_Node_level + 1 # 如果左子树有，那么左子树层数+1

            if right != None:
                bfs_queue.append(right)
                bfs_dic[right] = Tree_Node_level + 1 # 右子树同理

            if Tree_Node_level > cur_Level: # 该层node全部遍历一次
                cur_Level_Node_num = 1 # 当前层node个数归1
                cur_Level = Tree_Node_level # 当前层变成下一层
            else: # 证明这层的node还没全遍历
                cur_Level_Node_num += 1 # 所以node个数++
            Max = max(Max, cur_Level_Node_num)  # 统计Max

        return Max

    def isBST(self, node): # 判断搜索二叉树（左中右依次增加），中序遍历结果是递增则是
        if node is None:
            return True

        self.isBST(node.left_child)
        self.isBST_queue.append(node)

        self.isBST(node.right_child)
        # 判断是否时递增
        if any(self.isBST_queue[i + 1].value <= self.isBST_queue[i].value for i in range(len(self.isBST_queue) - 1)):
            return False
        else:
            return True


    def height(self, node): # 用于求是否时平衡二叉树（左右两颗子树高度差不超过1）
        if node is None:
            return 0

        left_height = self.height(node.left_child)
        right_height = self.height(node.right_child)

        return max(left_height, right_height) + 1

    # 是否是平衡二叉树（左右树高度差不超过1）
    def Is_Balance_Tree(self, node):
        if node is None:
            return True

        left = self.height(node.left_child)
        right = self.height(node.right_child)

        if abs(left - right) > 1:
            return False
        else:
            # 左树是平衡二叉树 and 右树是平衡二叉树 => 整体就是平衡二叉树
            return self.Is_Balance_Tree(node.left_child) and self.Is_Balance_Tree(node.right_child)

    # 判断是否是完全二叉树
    def Is_CLP(self, node):

        if node is None:
            return True
        queue = []
        leaf = False
        queue.append(node)

        while len(queue) != 0:
            Tree_node = queue.pop(0)
            left = Tree_node.left_child
            right = Tree_node.right_child

            # 任何一个节点，有右无左直接False
            # 遇到第一个孩子左右不双全节点，之后遍历的节点一定都是叶节点，否则False
            if ((left is None) and (right is not None)) or (leaf and (left is not None or right is not None)):
                return False

            # 遇到第一个孩子左右不双全节点，leaf = True
            if left is None or right is None:
                leaf = True

            if left is not None:
                queue.append(left)
            if right is not None:
                queue.append(right)

        return True

    # 用于判断满二叉树
    def Node_num(self, node):
        if node == None:
            return

        self.Node_num_queue.append(node)
        self.Node_num(node.left_child)
        self.Node_num(node.right_child)

        return len(self.Node_num_queue)


    def Is_Full(self, node): # 满二叉树判断条件：Node个数 = 2^level - 1

        if node == None:
            return

        Height = self.height(node)
        Node_num = self.Node_num(node)

        if Node_num == 2**Height - 1:
            return True
        else:
            return False

    def Lowest_Common_Ancestor(self, node, O1, O2):
        # node = None 代表这棵树上没有O1也没O2，返回node
        # node = O1 代表这棵树上只有O1，那么就返回O1
        # node = O2 代表这棵树上只有O2，那么就返回O2
        if node == None or node.value == O1 or node.value == O2:
            return node

        left = self.Lowest_Common_Ancestor(node.left_child, O1, O2)
        right = self.Lowest_Common_Ancestor(node.right_child, O1, O2)

        if left != None and right != None: # 如果这棵树上既有O1又有O2则返回O1和O2最低公共祖先节点
            return node
        elif left != None: # 如果这棵树上只有O1则返回O1
            return left
        else:
            return right   # 如果这棵树上只有O2则返回O2


    # 寻找某个节点的后继节点，用中序遍历找出这个数，它的下一个数即是他的后继 O(N)
    def Successor_Node_In_Order_Traverse(self, node, X):
        if node == None:
            return

        self.Successor_Node_In_Order_Traverse(node.left_child, X)
        self.Successor_Node_queue.append(node)
        self.Successor_Node_In_Order_Traverse(node.right_child, X)

        return self.Successor_Node_queue

    def _Successor_Node(self, node, X):
        In_Order_Traverse_Queue = self.Successor_Node_In_Order_Traverse(node, X)
        for i in range(len(In_Order_Traverse_Queue) - 1):
            if In_Order_Traverse_Queue[i].value == X:
                return In_Order_Traverse_Queue[i + 1]

    # 树用先序序列化(把树转换成字符串)
    # None记作#，用_分割
    # e.g. 0_1_3_7_#_#_8_#_#_4_9_#_#_#_2_5_#_#_6_#_#_
    def Serial_By_Pre_Order(self, node):
        if node == None:
            return '#_'

        string = str(node.value) + '_'
        string += self.Serial_By_Pre_Order(node.left_child)
        string += self.Serial_By_Pre_Order(node.right_child)
        return string

    # 把字符串以'_'分割开，返回list
    def Split_Str_Into_List(self, Pre_str):
        string_values_list = Pre_str.split('_')
        # 最后一个字符是'_'，所以pop出去
        string_values_list.pop(-1)

        return string_values_list

    # 先序序列化的树也只能用先序反序列化，同样依照先序遍历重新生成树
    # 中序，后续，也是一样，只不过把'Re_Serial_node = Node(int(value))' 位置改变即可
    def Re_Serial_By_Pre_Order(self, string_values_list):

        value = string_values_list.pop(0)
        if value == '#':
            return

        Re_Serial_node = Node(int(value))
        Re_Serial_node.left_child = self.Re_Serial_By_Pre_Order(string_values_list)
        Re_Serial_node.right_child = self.Re_Serial_By_Pre_Order(string_values_list)

        return Re_Serial_node

    # 按层序列化
    def Serial_By_Level(self, node):
        if node == None:
            return '#_'

        string = str(node.value) + '_'
        queue = [node]

        while len(queue) != 0:
            Tree_node = queue.pop(0)
            if Tree_node.left_child != None:
                string += str(Tree_node.left_child.value) + '_'
                queue.append(Tree_node.left_child)
            else:
                string += '#_'

            if Tree_node.right_child != None:
                string += str(Tree_node.right_child.value) + '_'
                queue.append(Tree_node.right_child)
            else:
                string += '#_'

        return string

    # 按层反序列化
    def Re_Serial_By_Level(self, string):
        string_value_list = string.split('_')

        index = 0 # 索引控制节点往下走
        queue = []
        root = self.Generate_Node_By_String(string_value_list[index])
        if root != None:
            queue.append(root)
        while len(queue) != 0:
            Tree_node = queue.pop(0)
            index += 1
            Tree_node.left_child = self.Generate_Node_By_String(string_value_list[index])
            index += 1
            Tree_node.right_child = self.Generate_Node_By_String(string_value_list[index])

            if Tree_node.left_child != None:
                queue.append(Tree_node.left_child)
            if Tree_node.right_child != None:
                queue.append(Tree_node.right_child)
        return root

    # 用来产生节点，按层反序列化专用
    def Generate_Node_By_String(self, value):
        if value == '#':
            return
        return Node(int(value))


    # 折纸问题，二叉树中序遍历问题，左侧头节点都是凹，右侧头节点都是凸
    def Folding_paper(self, N):

        self.Folding(1, N, True) # 头节点再第一层，折N次，凹为True

    def Folding(self, i, N, Down): # 中序遍历
        if i > N: # 头节点不会超过N层，超过了返回空
            return

        self.Folding(i + 1, N, True)
        print('Down' if Down else 'Up')
        self.Folding(i + 1, N, False)





















if __name__ == '__main__':
    values = [0,1,2,3,4,5,6]
    tree = Tree()
    for i in values:
        tree.add(i)
    #
    # tree.Pre_In_Post_Order_Traverse(tree.root)
    print(tree.Get_MAX_Width(tree.root))
    #print(tree.isBST(tree.root))
    #print(tree.height(tree.root))
    #print(tree.Is_Balance_Tree(tree.root))
    #print(tree.Is_CLP(tree.root))
    #print(tree.Is_Full(tree.root))
    #print(tree.Lowest_Common_Ancestor(tree.root, 7, 9))
    #print(tree._Successor_Node(tree.root, 3))
    #print(tree.Serial_By_Pre_Order(tree.root))
    #print(tree.Split_Str_Into_List('0_1_3_7_#_#_8_#_#_4_9_#_#_#_2_5_#_#_6_#_#_'))
    #tree.Re_Serial_By_Pre_Order(['0', '1', '3', '7', '#', '#', '8', '#', '#', '4', '9', '#', '#', '#', '2', '5', '#', '#', '6', '#', '#'])
    #print(tree.Serial_By_Level(tree.root))
    #print(tree.Re_Serial_By_Level('0_1_2_3_4_#_#_#_#_#_#_'))
    #tree.Folding_paper(3)


class Node():
    def __init__(self, value = None):
        self.value = value
        self.In = 0
        self.Out = 0
        self.next_node = []
        self.edge = []

def bfs(Node):
    queue = []
    dic = {}
    queue.append(Node)
    dic[Node] = True

    while len(queue) != 0:
        cur = queue.pop(0)
        print(cur.value)
        for i in cur.next_node:
            if not dic.get(i):
                dic[i] = True
                queue.append(i)
# 只用递归，不申请额外数据结构，如何逆序一个栈
def reverse(stack):
    if len(stack) == 0:
        return
    # i每次都接受list的第一个元素
    i = Get_And_Remove_Last_Element(stack)
    # stack就剩下除了第一个元素的剩下的list
    reverse(stack)
    # 最后全部执行完后，系统储存了3个i，e.g. i=3，i=2，i=1
    # 所以[3] -> [3,2] -> [3,2,1]
    stack.append(i)
    return stack
'''
原理与java版本没有什么区别，可是实现起来稍微有点区别
Get_And_Remove_Last_Element的主要区别是：

java版本是每一次都把一个栈的栈底元素拿出来，返回到reverse函数，再往栈里添加元素，实现了栈的逆序
e.g. 栈是[1,2,3]，先拿出1，返回reverse，再拿出2，返回reverse，再3，返回到reverse时候，先往栈里加入1，再2，再3，变成[3,2,1]，实现了逆序

python版本是每一次都把list的最后一个元素拿出来，返回到reverse函数，再往list里添加元素，实现了逆序
e.g. list是[1,2,3]，先拿出3，返回reverse，再2，返回reverse，再1，返回reverse时候，先往list里加入3，2，1变成[3,2,1]，实现了逆序

两个版本的主要区别就是利用栈和list的不同机制，往栈里添加元素，直接添加到栈底，而往list添加元素直接添加到list的第一位，所以正好
list和栈是相反的
主要利用了递归时，系统栈自动为你储存数字

'''

def Get_And_Remove_Last_Element(stack):
    # 每次pop出的都是list的最后一个元素
    result = stack.pop()
    if len(stack) == 0:
        # stack空时，往上返回最后pop出去的元素也就是list中第一个元素 e.g. return 1
        return result
    else:
        # 这里first实际是每次list的第一个元素
        # 因为list的append和栈的push机制的不同，所以也是正确的
        first = Get_And_Remove_Last_Element(stack)
        '''
        把除了list第一个元素的剩下的元素重新加入list，用于下次执行
        
        因为最后一个元素已经返回了，所以result此时是倒数第二个元素 e.g. result = 2
        因为倒数第二个元素已经返回了，所以result此时是倒数第三个元素 e.g. result = 3
        stack = [2,3]
        stack = [3]
        '''
        stack.append(result)
        # 每次都return出list的第一个元素
        return first

def main():
    print(reverse([1,2,3]))

if __name__ == '__main__':
    main()


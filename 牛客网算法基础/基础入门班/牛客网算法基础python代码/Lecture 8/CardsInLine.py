def win1(arr):
    if arr == None or len(arr) == 0:
        return 0
    '''
    在[0...n-1]上先手就是玩家1
    在[0...n-1]上后手就是玩家2
    返回玩家1和玩家2较大的那个
    '''
    return max(First_hand(arr, 0, len(arr) - 1), Second_hand(arr, 0, len(arr) - 1))

def First_hand(arr, i, j):
    # 这个[i...j]范围内只有一个数，并且我是先手，所以直接拿走
    if i == j:
        return arr[i]
    '''
    下面就是获得的分数
    arr[i]是已经拿到左侧牌的分数，然后再拿就是后手了
    Second_hand(arr, i + 1, j) 是后手情况下我能得到的最大分数
    
    或者：
    
    可以选择拿走右侧的纸牌
    arr[j]就是已经拿到的右侧纸牌的分数
    Second_hand(arr, i, j - 1) 是后手情况下我拿右侧纸牌获得的最大分数
    '''
    return max(arr[i] + Second_hand(arr, i + 1, j), arr[j] + Second_hand(arr, i, j - 1))

def Second_hand(arr, i, j):
    # 只有一个数，我又是后手，所以被对方拿走了，得到0
    if i == j:
        return 0
    '''
    两个尝试函数相互嵌套
    
    对方拿走i上的数（也就是左侧的数），那么就轮到我在[i + 1...j]上我先手了
    对方拿走j上的数（也就是右侧的数），那么就轮到我在[i...j - 1]上我先手了
    上面的是对方决定的，对方是决定对我最不利的，所以最小值是我的答案，因为别人会把最差的情况给我
    '''
    return min(First_hand(arr, i + 1, j), First_hand(arr, i, j - 1))

def main():
    print(win1([1, 2, 100, 4]))

if __name__ == '__main__':
    main()
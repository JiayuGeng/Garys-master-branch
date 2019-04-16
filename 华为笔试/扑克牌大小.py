poker_face = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
def judge(string):#判断左右手分别有几张牌面
    if len(string) == 1:
        return 1
    elif len(string) ==2:
        # 如果手里是两张牌，并且是双王，则是最大，返回最大值6
        if (string[0] =='joker' and string[1] == 'JOKER') or (string[1] =='joker' and string[0] == 'JOKER'):
            return 6
        # 如果是一个对，就返回2
        else:
            return 2
    elif len(string) == 3:
        return 3
    elif len(string) == 4:
        return 4
    else:
        return 5
def prin(string):
    for i in range(len(string)):
        if i == 0:
            print(string[i],end='')
        else:
            print(' '+string[i],end='')
    print()
while True:
    try:
        left,right = input().split('-')
        left = left.split(' ')
        right = right.split(' ')
        left_lei = judge(left)
        right_lei = judge(right)
        # 排数相等情况，只能是对2，三个3这种，所以比较第一张牌就知道大小了
        # 这里牌数相等的可以看作所有牌都是一种
        if left_lei == right_lei:
            if poker_face.index(left[0])<poker_face.index(right[0]):
                prin(right)
            else:
                prin(left)
        # 谁是对王谁大
        elif left_lei ==6 or right_lei == 6:
            if left_lei ==6:
                prin(left)
            else:
                prin(right)
        # 四个牌也是炸弹，谁是4个谁大
        elif left_lei ==4 or right_lei ==4:
            if left_lei ==4:
                prin(left)
            else:
                prin(right)
        # 其他情况都比较不了
        else:
            print("ERROR")
    except:
        break
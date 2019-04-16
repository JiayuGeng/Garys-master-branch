
def process(pre, in_, after):
    # 没有待进站的，也没有待出站的车，一种情况产生了
    if not pre and not in_:
        res.append(' '.join(after))
    # 递推关系为对于当前情况有让下一辆火车进站或让站中的一辆火车出站两种可能，对于两种可能分别调用递归函数，即可得出问题的解。
    if in_: # 让站中的一辆火车出站。出站作业，先检查站内是否有车（先出栈）
        after.append(in_.pop())
        process(pre, in_, after)
        in_.append(after.pop())
    if pre: # 进站作业，先检查是否还有待进站车辆 （再入栈）
        in_.append(pre.pop(0))
        process(pre, in_, after)
        pre.insert(0, in_.pop())

while 1:
    try:
        num = int(input())
        pre = input().split()  # 待进站的车辆

        in_, after, res = [], [], [] # 站内火车，出站后的火车，结果
        process(pre, in_, after)
        res.sort() # 要求字典序
        for i in res:
            print(i)
    except:
        break










# def handle(pre, in_, after):
#     if not pre and not in_:  # 没有待进站的，也没有待出站的车，一种情况产生了
#         result.append(" ".join(after))
#     # 递推关系为对于当前情况有让下一辆火车进站或让站中的一辆火车出站两种可能，对于两种可能分别调用递归函数，即可得出问题的解。
#     if in_pre:  # 让站中的一辆火车出站。出站作业，先检查站内是否有车
#         after.append(in_.pop())
#         handle(pre, in_, after)
#         in_.append(after.pop())
#     if pre:  # 进站作业，先检查是否还有待进站车辆
#         in_.append(pre.pop(0))
#         handle(pre, in_, after)
#         pre.insert(0, in_.pop())
#
#
# while True:
#     try:
#         # n = input()
#         # pre = input().split()  # 待进站的车辆
#         n = 3
#         pre = ['1', '2', '3']
#         in_pre = []  # 站中火车
#         after = []  # 出站后的车辆
#         result = []
#         handle(pre, in_pre, after)
#         result.sort()  # 要字典序输出，排个序咯
#         for i in result:
#             print(i)
#     except:
#         break
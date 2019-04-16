import sys # 输入是一起输入的

# def process(twokey, a, result):
#     count = 0
#     index = 0
#     for y in twokey:
#         # 如果输入的order的第一个和第二个字母都能匹配上上方字典里的字母，count+1
#         if a[0] == y.split()[0][:len(a[0])] and a[1] == y.split()[1][:len(a[1])]:
#             count += 1
#             index = twokey.index(y)
#     # count > 1说明匹配出两个字典里的命令，不符合题目要求
#     # count = 0说明没有匹配出字典里的命令
#     if count > 1 or count == 0:
#         print('unknown command')
#     # 只有当只找到一个匹配成功时，输出
#     elif count == 1:
#         print(result[index])
#
#
#
# onekey = 'reset'
# twokey = ['reset board', 'reboot backplane', 'backplane abort', 'board add', 'board delet']
# result = ['board fault', 'impossible', 'install first', 'where to add', 'no board at all']
#
# for i in sys.stdin:
#     a = i.strip().split()
#     l = len(a)
#     if l <= 0 or l >= 3:
#         print('unknown command')
#     elif l == 1:
#         # 因为只要reset一个指令是一个单词的order，所以如果输入的order的字母能在reset匹配上order长度的字符，就是匹配成功
#         # :len(one_order[0])就是看order长度的指令和reset同长度是否能匹配
#         if a[0] == onekey[:len(a[0])]:
#             print('reset what')
#         else:
#             print('unknown command')
#     elif l == 2:
#         process(twokey, a, result)

def checkTwoKeys(twoKeys, a, result):
    count = 0
    index = 0
    for y in twoKeys:
        if a[0] == y.split()[0][:len(a[0])] and a[1] == y.split()[1][:len(a[1])]:
            count += 1
            index = twoKeys.index(y)
    if count > 1 or count == 0:
        print("unkown command")
    elif count == 1:
        print(result[index])


oneKey = 'reset'
twoKeys = ['reset board', 'reboot backplane', 'backplane abort', 'board add', 'board delete']
result = ['board fault', 'impossible', 'install first', 'where to add', 'no board at all']
for i in sys.stdin:
    a = i.strip().split()
    l = len(a)
    if l <= 0 or l >= 3:
        print("unkown command")
    elif l == 1:
        if a[0] == oneKey[:len(a[0])]:
            print("reset what")
        else:
            print("unkown command")
    elif l == 2:
        checkTwoKeys(twoKeys, a, result)

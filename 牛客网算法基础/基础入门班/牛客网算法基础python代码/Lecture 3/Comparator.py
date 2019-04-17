from heapq import *

'''
这个暂时不会。。。
'''
def Ascending_Compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

def Descending_Compare(x, y):
    if y < x:
        return -1
    elif y > x:
        return 1
    else:
        return 0

def Preority_Queue(Ascending_Compare):
    h = []
    heappush(h, 2)
    heappush(h, 1)
    heappush(h, 3)
    while len(h) != 0:
        heappop(h)

if __name__ == '__main__':
    print(Ascending_Compare(1 ,2))

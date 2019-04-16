money, item = map(lambda x: int(x), input().split(' '))
print(item)
item_list = []
for _ in range(item):
    m, b, i = map(lambda x: int(x), input().split(' '))
    item_list.append([m, b, i])

def solution(money, item, item_list):
    a = [[0] * (money + 1) for _ in range(m + 1)]
    for i in range(1, item + 1):
        for j in range(1, money + 1):
            # 如果商品价格小于总钱数
            if item_list[i - 1][0] <= j:
                # 所获的最大的收益就是不买和买中取最大值
                a[i][j] = max(a[i-1][j], a[i-1][j-item_list[i-1][0]] + item_list[i-1][0]*item_list[i-1][1])
    return a

if __name__ == '__main__':
    print(solution(money, item, item_list))

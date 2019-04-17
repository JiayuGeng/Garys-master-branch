# 01背包问题

def Max_Value(weights, values, bag):
    return process(weights, values, 0, 0, 0, bag )

def process(weights, values, i, alreadyWeight, alreadyValue, bag):
    # 如果装的重量大于背包重量了，就return 0
    if alreadyWeight > bag:
        return 0
    # i走完了所以货物的重量，就说明能装的都装了，return已经装下的价值，结束
    if i == len(weights):
        return alreadyValue
    '''
    分为两种情况，要货物还是不要货物
    第一种是不要的，所以递归下去除了i变成下一个货物，其他不变
    第二种是要的，所以除了i变成下一个货物，背包已经装的重量也得增加，已经有的价值也得增加
    '''
    return max(process(weights, values, i + 1, alreadyWeight, alreadyValue, bag),
               process(weights, values, i + 1, alreadyWeight + weights[i], alreadyValue + values[i], bag))

def main():
    weights = [3, 2, 4, 7]
    values = [5, 6, 3, 19]
    bag = 11
    print(Max_Value(weights, values, bag))

if __name__ == '__main__':
    main()
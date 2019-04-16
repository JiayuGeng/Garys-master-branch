import sys

while True:
    try:
        priceGoods = {'A1': 2, 'A2': 3, 'A3': 4, 'A4': 5, 'A5': 8, 'A6': 6}
        priceMoney = [1, 2, 5, 10]
        numGoods = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0}
        numMoney = [0] * 4
        # 1 2 5 10
        balance = 0


        def printMoney(line):
            print('1 yuan coin number=%s' % (line[0]))
            print('2 yuan coin number=%s' % (line[1]))
            print('5 yuan coin number=%s' % (line[2]))
            print('10 yuan coin number=%s' % (line[3]))


        def printGoods(priceGoods, numGoods, flag):  # 0:sorted goods name;1:sorted num of goods
            if flag == 0:
                for i in range(6):
                    good = 'A' + str(i + 1)
                    print(good + ' ' + str(priceGoods[good]) + ' ' + str(numGoods[good]))
            if flag == 1:
                print(numGoods)
                numGoodsSorted = sorted(numGoods.items(), key=lambda a: a[1], reverse=True)
                for i in range(6):
                    print(numGoodsSorted[i][0] + ' ' + str(priceGoods[numGoodsSorted[i][0]]) + ' ' + str(
                        numGoodsSorted[i][1]))


        line = input().split(';')[:-1]
        for i in line:
            func = i.split()
            if func[0] == 'r':
                func[1] = func[1].split('-')
                for i in range(6):
                    numGoods['A' + str(i + 1)] += int(func[1][i])
                for i in range(4):
                    numMoney[i] += int(func[2].split('-')[i])  # 1 2 5 10
                print('S001:Initialization is successful')
            elif func[0] == 'p':
                if int(func[1]) not in priceMoney:
                    print('E002:Denomination error')
                elif int(func[1]) in [5, 10] and numMoney[0] + numMoney[1] * 2 < int(func[1]):
                    print('E003:Change is not enough, pay fail')
                elif int(func[1]) == 10 and balance > 10:  # only print when $10 input
                    print('E004:Pay the balance is beyond the scope biggest')
                elif numGoods['A1'] == numGoods['A2'] == numGoods['A3'] == numGoods['A4'] == numGoods['A5'] == numGoods[
                    'A6'] == 0:
                    print('E005:All the goods sold out')
                else:
                    numMoney[priceMoney.index(int(func[1]))] += 1
                    balance += int(func[1])
                    print('S002:Pay success,balance=%d' % (balance))
            elif func[0] == 'b':
                if func[1] not in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']:
                    print('E006:Goods does not exist')
                elif numGoods[func[1]] == 0:
                    print('E007:The goods sold out')
                elif balance < priceGoods[func[1]]:
                    print('E008:Lack of balance')
                else:
                    balance -= priceGoods[func[1]]
                    numGoods[func[1]] -= 1
                    print('S003:Buy success,balance=%d' % (balance))
            elif func[0] == 'c':
                if balance == 0:
                    sys.stdout.write('E009:Work failure')  # no line break
                else:
                    numCall = [0] * 4  # 1 2 5 10
                    for i in range(-1, -5, -1):
                        numCall[i] = min(balance // priceMoney[i], numMoney[i])
                        balance -= numCall[i] * priceMoney[i]
                        numMoney[i] -= numCall[i]
                    printMoney(numCall)
                    balance = 0
            elif func[0] == 'q':
                if func[1] == '0':
                    printGoods(priceGoods, numGoods, 1)
                elif func[1] == '1':
                    printMoney(numMoney)
            else:
                sys.stdout.write('E010:Parameter error')  # no line break
    except:
        break
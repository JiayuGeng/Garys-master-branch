
def process(num):
    less_20 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    less_100 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if num < 20:
        return less_20[num - 1: num]
    elif num < 100:
        return [less_100[num // 10 - 2]] + process(num % 10)
    elif num < 1000:
        return [less_20[num // 100 - 1]] + ['hundred'] + ['and'] + process(num % 100)

    for index, word in enumerate(('thousand','million','billion'), 1):
        # 从num < 一百万，十亿开始判断
        if num < 1000 ** (index + 1):
            return process(num // (1000 ** index)) + [word] + process(num % (1000 ** index))
def main():
    num = int(input())

    if num == 0:
        return 'zero'
    else:
        return ' '.join(process(num))

while True:
    try:
        print(main())
    except:
        break



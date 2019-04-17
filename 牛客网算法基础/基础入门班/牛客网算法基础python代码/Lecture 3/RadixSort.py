import sys
'''
基数排序：基于10进制的排序，从个位开始，个位上数字是多少入多少标号的桶，十位，百位...
count详细说明下边注释有写，count是为了从后往前往bucket里排序放数字时决定数字的位置
e.g. arr = [2,4,1,5,3] 此时d = 1，代表个位，count[3] = 3代表在个位上是0，1，2，3这三个数的数字有3个（1，2，3）
当往bucket里放的时候从arr的最后一个数3开始拿，拿出的3放在bucket中的第（count[3] - 1 = 2）位上
此时得到的bucket是按照数字的个位排好序的，就是按照个位数字大小的排序。如果有十位，在进行第二轮按十位上的数字基于个位上
数字接着排序，注意是基于个位，十位上排序不会影响个位上之前排好的顺序，百位同理。

因为我们正常比较数的大小都是从高位（这里是百位）到低位（这里是个位）比较，所以放数字位置的时候，应该从个位从小到大，
十位从小到大，百位从小到大这么放，如果先放了高位的从小到大，再放低位的从小到大，得到的结论就是错的。

基数排序关键点:
1. count是某一位上从0...i的数有多少，具体见下面解释。count就是记录每一位上的数在数组的第几个位置，先个位，十位，百位...
    e.g.[...327]，arr最后一个数是327，现在考虑个位，假设count[7] = 100, 那么327就放在bucket里面（count[7] - 1 = 99）位置上，
    证明前面有98个数的个位是0～6的。
2. 往bucket里放的时候，一定是倒叙放（先放数组最后一个数...第一个数）
3. 其他的比如得到这个数字百位上的数之类的都是小骚操作

e.g.
arr = [156,143,111,175,132]

count个位数完啦：
[0, 1, 2, 3, 3, 4, 5, 5, 5, 5]
实时的bucket变化： [None, 132, None, None, None]
实时的bucket变化： [None, 132, None, 175, None]
实时的bucket变化： [111, 132, None, 175, None]
实时的bucket变化： [111, 132, 143, 175, None]
实时的bucket变化： [111, 132, 143, 175, 156]
bucket个位放完啦：
[111, 132, 143, 175, 156]

count十位数完啦：
[0, 1, 1, 2, 3, 4, 4, 5, 5, 5]
实时的bucket变化： [111, 132, 143, 156, 156]
实时的bucket变化： [111, 132, 143, 156, 175]
实时的bucket变化： [111, 132, 143, 156, 175]
实时的bucket变化： [111, 132, 143, 156, 175]
实时的bucket变化： [111, 132, 143, 156, 175]
bucket十位放完啦：
[111, 132, 143, 156, 175]

count百位数完啦：
[0, 5, 5, 5, 5, 5, 5, 5, 5, 5]
实时的bucket变化： [111, 132, 143, 156, 175]
实时的bucket变化： [111, 132, 143, 156, 175]
实时的bucket变化： [111, 132, 143, 156, 175]
实时的bucket变化： [111, 132, 143, 156, 175]
实时的bucket变化： [111, 132, 143, 156, 175]
bucket百位放完啦：
[111, 132, 143, 156, 175]

最终结果出来啦：
[111, 132, 143, 156, 175]

'''

def radixSort(arr):
    if arr == None or len(arr) < 2:
        return
    process(arr, 0, len(arr) - 1, maxbits(arr))
    return arr

# arr[begin...end]排序
# digit 是最大位数

def process(arr, begin, end, digit):
    radix = 10
    bucket = [None] * (end - begin + 1) # 多少个数就准备多少空间
    m = 0
    for d in range(1, digit + 1): # 有多少位就进出桶几次，个位，十位，百位
        '''
        10个空间
        count[0] 当前位（d位）是0的数字有多少个
        count[1] 当前位（d位）是（0和1）的数字有多少个
        count[2] 当前位（d位）是（0，1，2）的数字有多少个
        count[i] 当前位（d位）是（0...i）的数字有多少个
        '''
        # m += 1
        count = [0] * radix
        for i in range(end + 1):
            j = getDigit(arr[i], d) # 每个数字，提取它d位上的数字给j
            count[j] += 1 # 计数++

        for i in range(1, radix):
            count[i] = count[i] + count[i - 1] #就是上面一大坨含义count[0..i]
        # if m == 1:
        #     print('count个位数完啦：')
        #     print(count)
        # elif m == 2:
        #     print('count十位数完啦：')
        #     print(count)
        # else:
        #     print('count百位数完啦：')
        #     print(count)
        for i in range(end - begin, -1, -1):
            j = getDigit(arr[i], d)
            bucket[count[j] - 1] = arr[i]
            # print('实时的bucket变化：',bucket)
            count[j] -= 1
        # if m == 1:
        #     print('bucket个位放完啦：')
        #     print(bucket)
        # elif m == 2:
        #     print('bucket十位放完啦：')
        #     print(bucket)
        # else:
        #     print('bucket百位放完啦：')
        #     print(bucket)
        j = 0
        for i in range(end + 1):
            arr[i] = bucket[j]
            j += 1

def getDigit(x, d):
    return int(x / (10 ** (d-1)) % 10)



def maxbits(arr): # 最大值有多少十进制的位
    Max = -sys.maxsize - 1 # Max给系统最小值，其实给arr[0]也可以，目的都是找出数组最大值
    for i in range(len(arr)):
        Max = max(Max, arr[i])

    res = len(str(Max))

    return res

def main():
    print(radixSort([156,143,111,175,132]))

if __name__ == '__main__':
    main()
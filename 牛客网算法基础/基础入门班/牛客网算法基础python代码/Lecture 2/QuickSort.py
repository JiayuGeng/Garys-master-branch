'''
written by Jiayu Geng 
19/01/2019

妞宝哥哥给你解释一下哈：

整个代码用了递归，传进去的arr先经过quickSort里的process，把<p放左边,=p放中间,>p放右边，但是
此时是无序的。
因为是递归，<=>这3个区直接的范围不断减少，所以最后就导致了只有三个数，就导致了有序的排列
然后分别再从处理完之后的arr的左，右，在进行重复的操作，直到所有数字按顺序排列

e.g. arr = [3,8,2,4,7,5,6] # 以6划分，<6都在6左边，=6在中间，>6在右边，此时无序
[3, 5, 2, 4, 6, 8, 7] # 以4划分，<4都在4左边，=4在中间，>4在右边，此时无序
[3, 2, 4, 5, 6, 8, 7] # 在对<4区进行上述操作，以5划分，同理
[2, 3, 4, 5, 6, 8, 7] # 在对<5区进行上述操作，以4划分，同理，<区此时排好序了，因为在<p,=p,>p时放数就是在排序。知道难理解，好好想想妞宝。
[2, 3, 4, 5, 6, 7, 8] # 开始进行>区的排序，同理
[2, 3, 4, 5, 6, 7, 8] # 这个是在quickSort里的打印，所以与上面一样，上面的打印是在partition里
'''

def partition(arr, l, r):
    less = l - 1 # <区右边界
    more = r # >区左边界，最后一个数最为划分值，把最后一个数包括进去了

    while l < more: # L表示当前数的位置 只要当前值不与>区碰到执行while
        if arr[l] < arr[r]: # 当前数<划分值p
            arr[l], arr[less + 1] = arr[less + 1], arr[l] # 当前数与<区后一个数交换
            less += 1 # <区右扩
            l += 1 # 当前数往后跳
        elif arr[l] > arr[r]:
            arr[l], arr[more - 1] = arr[more - 1], arr[l] # >区前一个数和l交换
            more -= 1 # >区左扩，当前数不变
        else:
            l += 1 # 否则就是当前数=划分值，直接l跳下一个

    arr[more], arr[r] = arr[r], arr[more] # 大于区左边界more与大于区最后一个数r交换
    # print(arr)

    return [less + 1, more] # 返回的是等于区左边界和右边界，在process中p[0]-1代表<区右边界，
                            # p[1] + 1是>区左边界，为的是process处理<区和>区

# arr[l...r] 上有序
def process(arr, l, r):
    if l < r:
        p = partition(arr, l, r) # p[0]是 = 区左边界，p[1]是=区右边界
        process(arr, l, p[0] - 1)  # <区
        process(arr, p[1] + 1, r) # >区


def quickSort(arr):
    if arr == None or len(arr) < 2:
        return
    process(arr, 0, len(arr) - 1)
    return arr

def main():
    print(quickSort([3,8,2,4,7,5,6]))

if __name__ == '__main__':
    main()


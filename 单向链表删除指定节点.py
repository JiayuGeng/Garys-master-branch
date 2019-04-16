while True:
    try:
        nums = list(map(str, input().split()))
        #nums = [5,2,3,2,4,3,5,2,1,4,3]
        linked_list = [nums[1]]

        for i in range(2, len(nums) - 1, 2):
            # 3，2 -> 在node=2的后面插入3；
            # 4，3 -> 在node=3的后面插入4；
            insert_node, pos_node = nums[i], nums[i + 1]
            # index(pos_node)是定位要插入的位置，也就是pos_node的下一个，所以+1
            linked_list.insert(linked_list.index(pos_node) + 1, insert_node)

        linked_list.remove(nums[-1])
        print(' '.join(linked_list) + ' ')
    except:
        break
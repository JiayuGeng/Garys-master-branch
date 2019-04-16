
while True:
    try:
        def process(apple, plate):
            if apple == 0 or plate == 1:
                return 1
            if plate > apple:
                return process(apple, apple)
            else:
                # 有一个盘子为空，其他盘子都有苹果
                # 也就是将apple个苹果放在plate-1个盘子上
                # +
                # 每一个盘子至少有一个苹果
                # 也就是每个盘子都有苹果，即剩下apple-plate个苹果，再放入plate个盘子中
                return process(apple, plate - 1) + process(apple - plate, plate)


        [apple, plate] = list(map(int, input().split()))
        print(process(apple, plate))
    except:
        break
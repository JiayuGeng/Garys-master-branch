while 1:
    try:
        one_str = input()

        cur_length = 0
        max_length = 0
        cur_str = ''
        max_arr = []
        for i, v in enumerate(one_str):
            if v.isdigit():
                cur_length += 1
                cur_str += v
                if cur_length > max_length:
                    max_length = cur_length
                    max_arr = [cur_str]
                elif cur_length == max_length:
                    max_arr.append(cur_str)
            else:
                cur_length = 0
                cur_str = ''
        print(''.join(max_arr) + ',' + str(max_length))
    except:
        break
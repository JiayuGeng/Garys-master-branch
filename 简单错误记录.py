import collections

# OrderedDict会根据放入元素的先后顺序进行排序
# 华为2016校招第二题
d = collections.OrderedDict()

while True:
    try:
        file_row = input().split()
        file_name = file_row[0].split('\\')[-1]
        row = file_row[1]
        if (file_name, row) not in d:
            d[(file_name, row)] = 1
        else:
            d[(file_name, row)] += 1
    except:
        break

error = d.items()
sort_dic = sorted(error, key=lambda x:x[1], reverse=True)
count = 0
for key, value in sort_dic:
    count += 1
    if count <= 8:
        name = key[0]
        if len(name) > 16:
            name = name[-16:]
        row = key[1]
        print(name + ' ' + row + ' ' + str(value))
    else:
        break




# import sys

# d = {}
# name = []
# while True:
#     # 此处应用标准输出去掉''
#     line = sys.stdin.readline().strip()
#     if line == '':
#         break
#
#     file = line.split(' ')
#     file_name = file[0].split('\\')[-1]
#     raw_num = file[1]
#
#     if len(file_name) > 16:
#         file_name = file_name[-16:]
#
#     record = file_name + ' ' + raw_num
#     if record not in d.keys():
#         name.append(record)
#         d[record] = 1
#     else:
#         d[record] += 1
#
# for item in name[-8:]:
#     print(item + ' ' + str(d[item]))

import sys

def check_valid(ip, mask):
    if len(ip) != 4 or len(mask) != 4:
        return False
    for i in ip:
        if not i.isdigit() or int(i) > 255 or int(i) < 0:
            return False

    s = ''
    for i in mask:
        if not i.isdigit() or int(i) > 255 or int(i) < 0:
            return False

        # 子网掩码转换成2进制看1之间是否有0，或者0之间是否有1
        # 0之间有1，或者1之间有0则不合法
        str1 = bin(int(i))[2:]
        # 子网掩码不够8位在前面补0
        str2 = (8 - len(str1)) * '0' + str1
        s += str2

    # 找到第一个0之后，看它后面的是否全是0，如果不是，false
    zeros = s[s.find('0'):]
    if int(zeros) != 0:
        return False
    return True


def divide(ip, res):
    first_ip = ip[0]
    second_ip = ip[1]
    if int(first_ip) == 10:
        res[5] += 1
    if int(first_ip) == 172 and 15 < int(second_ip) < 32:
        res[5] += 1
    if int(first_ip) == 192 and int(second_ip) == 168:
        res[5] += 1
    if 0 < int(first_ip) < 127:
        res[0] += 1
    elif 127 < int(first_ip) < 192:
        res[1] += 1
    elif 191 < int(first_ip) < 224:
        res[2] += 1
    elif 223 < int(first_ip) < 240:
        res[3] += 1
    elif 239 < int(first_ip) < 256:
        res[4] += 1

res = [0, 0, 0, 0, 0, 0]
wrong = 0

while True:
    strings = sys.stdin.readline().strip()
    if strings == '':
        break
    line = strings.split('~')
    ip = line[0].split('.')
    mask = line[1].split('.')

    if check_valid(ip, mask):
        divide(ip, res)
    else:
        wrong += 1

print('{} {} {} {} {} {} {}'.format(res[0], res[1], res[2], res[3], res[4], wrong, res[5]))

# l = ['10.70.44.68~255.254.255.0', '1.0.0.1~255.0.0.0', '192.168.0.2~255.255.255.0', '19..0.~255.255.255.0']
# for i in range(4):
#     strings = l[i]
#     line = strings.split('~')
#     ip = line[0].split('.')
#     mask = line[1].split('.')
#
#     if check_valid(ip, mask):
#         divide(ip, res)
#     else:
#         wrong += 1
#
# print('{} {} {} {} {} {} {}'.format(res[0], res[1], res[2], res[3], res[4], wrong, res[5]))



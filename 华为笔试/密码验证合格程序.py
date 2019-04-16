import sys

def check_1(line):
    if len(line) <= 8:
        return False
    else:
        return True

def check_2(line):
    digit, upper, lower, symbol = 0, 0, 0, 0
    for i in line:
        if i.isdigit():
            digit = 1
        elif i.isupper():
            upper = 1
        elif i.islower():
            lower = 1
        else:
            symbol = 1

    if digit + upper + lower + symbol >= 3:
        return True
    else:
        return False

def check_3(line):
    for i in range(len(line) - 3):
        if line.count(line[i: i+3]) > 1:
            return False
    return True


while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break

    if check_1(line) and check_2(line) and check_3(line):
        print('OK')
    else:
        print('NG')

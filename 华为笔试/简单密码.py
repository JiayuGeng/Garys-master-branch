import sys

while True:
    password = sys.stdin.readline().strip()
    if password == '':
        break
    res = ''
    for i in password:
        if i.isupper():
            if i == 'Z':
                res += 'a'
            else:
                l = i.lower()
                res += chr(ord(l) + 1)
        elif i.islower():
            if i in 'abc':
                res += '2'
            elif i in 'def':
                res += '3'
            elif i in 'ghi':
                res += '4'
            elif i in 'jkl':
                res += '5'
            elif i in 'mno':
                res += '6'
            elif i in 'pqrs':
                res += '7'
            elif i in 'tuv':
                res += '8'
            elif i in 'wxyz':
                res += '9'

        elif i == '1':
            res += '1'
        elif i == '0':
            res += '0'
        else:
            res += i

    print(res)


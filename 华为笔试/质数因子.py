def prime(num):
    if num == 2:
        return num
    else:
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                return num

n = int(input())
s = ''
i = 2
while i <= n:
    if n % i == 0 and prime(i) != None:
        n /= i
        s += str(i) + ' '
        i = 2
    else:
        i += 1

print(s)


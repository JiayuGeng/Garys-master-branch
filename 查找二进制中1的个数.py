while True:
    try:
        print(bin(int(input())).count('1'))
    except:
        break
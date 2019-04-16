while True:
    try:
        encode = input()
        decode = input()

        encode_res = ''
        for i in encode:
            if i.isalpha():
                if i == 'z':
                    encode_res += 'A'
                elif i == 'Z':
                    encode_res += 'a'
                else:
                    if i.islower():
                        encode_res += chr(ord(i) + 1).upper()
                    else:
                        encode_res += chr(ord(i) + 1).lower()
            else:
                if i == '9':
                    encode_res += '0'
                else:
                    encode_res += str(int(i) + 1)

        decode_res = ''
        for i in decode:
            if i.isalpha():
                if i == 'a':
                    decode_res += 'Z'
                elif i == 'A':
                    decode_res += 'z'
                else:
                    if i.islower():
                        decode_res += chr(ord(i) - 1).upper()
                    else:
                        decode_res += chr(ord(i) - 1).lower()
            else:
                if i == '0':
                    decode_res += '9'
                else:
                    decode_res += str(int(i) - 1)
        print(encode_res)
        print(decode_res)

    except:
         break



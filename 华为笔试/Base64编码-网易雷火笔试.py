import base64, string

'''
Base64编码表由64个字符组成，编码后的字符由表中字符组合而成，流程如下： 
1. base64的编码都是按字符串长度，以每3个8bit的字符为一组。 
2. 然后针对每组，首先获取每个字符的ASCII编码。 
3. 然后将ASCII编码转换成8bit的二进制，得到一组3*8=24bit的字节。 
4. 然后再将这24bit划分为4个6bit的字节，并在每个6bit的字节前面都填两个高位0，得到4个8bit的字节。 
5. 然后将这4个8bit的字节转换成10进制，对照Base64编码表，得到对应编码后的字符。 
注： 
• 由于要求被编码字符是8bit，所以须在ASCII编码范围内，\u0000-\u00ff，中文就不行。 
• 由于2^6=64，而以1个6bit为一个单元，因此一定能在0~63的编码表中找到对应的编码！ 
'''

base64_charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

def encode(origin_byte):
    # 将每一位bit转换成二进制字符串
    base64_byte = [''.format(bin(int(b)).replace('0b', '')) for b in origin_byte]

    resp = ''
    # len(base64_byte)代表有几个元素
    # e.g. 'lucy'有4个元素，base64_byte = ['001010101','010101010', '01010101', '0101010']
    nums = len(base64_byte) // 3
    remain = len(base64_byte) % 3

    # 不能被整除的最后一部分不是整数部分，填入inte_part里面
    intergal_part = base64_byte[0:3 * nums]

    while intergal_part:
        # 取3个字节，以每6bit转换为4个整数
        tmp_unit = ''.join(intergal_part[0:3])
        tmp_unit = [int(tmp_unit[x: x + 6], 2) for x in [0, 6, 12, 18]]
        # 按照之前做好的表，取对应base64字符
        resp += ''.join([base64_charset[i] for i in tmp_unit])
        # intergal_part后移3个，继续上面操作
        intergal_part = intergal_part[3:]

    # 走下面的if就说明不能被3整除，也就是有剩余的，也就是需要补0
    if remain:
        # 补齐3个字节，每个字节补充0000 0000
        remain_part = ''.join(base64_byte[3 * nums:]) + (3 - remain) * '0' * 8
        # 取3个字节，以每6bit转换为4个整数
        # 剩余1个字节可构造2个base64字符，补充'=='；剩余2字节可构造3个base64字符，补充'='
        tmp_unit = [int(remain_part[x : x + 6], 2) for x in [0, 6, 12, 18]][:remain + 1]
        resp += ''.join([base64_charset[i] for i in tmp_unit]) + (3 - remain) * '='
    return resp


print(encode('01101001001100101100010101'))
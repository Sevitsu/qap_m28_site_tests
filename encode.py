# Encoding string of cyrillic characters into hex
def convert_str_hex(string='') -> str:
    msg = string
    result = msg.encode('utf-8').hex().upper()
    res = '%'
    j = 0
    for i in range(len(result)):
        res = res + result[i]
        j += 1
        if j == 2:
            res = res + '%'
            j = 0
    res = res.removesuffix('%')
    return res

# 大小寫互換

# python 的 ASCII function
# ord('s')：獲得s的ASCII值，print(ord('s'))
# chr(s)：獲得數字 s 對應的字母，print(chr(115))

# a-z :97-112
# A-Z :65-90

string = 'AbcD'
new_str = ''

for i in range(len(string)):

    # 大寫
    if ord(string[i]) >= 65 and ord(string[i]) <= 90:
        new_str += str(chr(ord(string[i])+32))

    # 小寫
    elif ord(string[i]) >= 97 and ord(string[i]) <= 122:
        new_str += str(chr(ord(string[i])-32))

    else:
        new_str += string


print(new_str)

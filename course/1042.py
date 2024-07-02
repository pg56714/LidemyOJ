# String toLowerCase
# https://oj.lidemy.com/problem/1042
# 給你一個字串 S，請你把 S 裡面出現的大寫英文字母都轉成小寫（禁止使用內建函式 toLowerCase）
# 輸入只有一行，為一個字串 S

# Sample Input 1
# AbC!!

# Sample Output 1
# abc!!


def to_lowercase(s):
    result = ""
    for char in s:
        if "A" <= char <= "Z":
            # ord獲取ASCII碼，chr獲取字符
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


input_string = input("")

lowercased_string = to_lowercase(input_string)
print(lowercased_string)

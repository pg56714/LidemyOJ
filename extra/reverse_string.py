# 字串反轉

string = input()
new_str = []

# 字串陣列反轉
for i in range(len(string)):
    new_str.append(string[len(string)-i-1])
    # print(new_str)

# 字串合併
new_comb = ''
for words in new_str:
    # print(words)
    new_comb += words

print(new_comb)

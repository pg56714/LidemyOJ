# 數字各位數加總

# 如果數字為 1234 那加總的結果是 1+2+3+4=10
# 數字為1111 加總結果為1+1+1+1=4
# 數字為-1111 加總結果為1+1+1+1=4

# 方法一-數字解
def addDigits(num):
    if (num < 0):
        num = num * -1

    sum = 0

    while num:
        sum += num % 10
        num //= 10

    print(sum)

# 方法二-字串解
# def addDigits(num):
#     if (num < 0):
#         num = num * -1

#     sum = 0

#     for i in str(num):
#         sum += int(i)

#     print(sum)


addDigits(11111)
addDigits(1234)
addDigits(-1234)

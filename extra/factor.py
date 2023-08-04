# 印出因數

input = 15

for i in range(1, input+1):
    # 15 / 1 餘 0、15 / 2 餘 1
    if input % i == 0:
        print(i)

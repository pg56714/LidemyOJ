# 題目：圈圈叉叉
# https://oj.lidemy.com/problem/1046
# 在一個 3*3 的格子上面依序填入 O 或是 X，先連成一線者獲勝

# 方法一
# input1 = input()
# input2 = input()
# input3 = input()
# win = []

# # 橫
# if input1[0] == input1[1] == input1[2]:
#     win.append(input1[0])
# if input2[0] == input2[1] == input2[2]:
#     win.append(input2[0])
# if input3[0] == input3[1] == input3[2]:
#     win.append(input3[0])


# # 直
# if input1[0] == input2[0] == input3[0]:
#     win.append(input1[0])
# if input1[1] == input2[1] == input3[1]:
#     win.append(input1[1])
# if input1[2] == input2[2] == input3[2]:
#     win.append(input1[2])

# # 左斜
# if input1[0] == input2[1] == input3[2]:
#     win.append(input1[0])

# # 右斜
# if input1[2] == input2[1] == input3[0]:
#     win.append(input1[2])

# if len(win) == 0:
#     print('DRAW')
# else:
#     print(win[0])

# 方法二
inputList = [input(), input(), input()]

# print(inputList)


def whoWin(inputList):
    for i in range(len(inputList)):
        if (inputList[i][0] == inputList[i][1] == inputList[i][2]):
            return inputList[i][0]

    for i in range(len(inputList)):
        if (inputList[0][i] == inputList[1][i] == inputList[2][i]):
            return inputList[0][i]

    # 左斜
    if inputList[0][0] == inputList[1][1] == inputList[2][2]:
        return inputList[0][0]

    # 右斜
    if inputList[0][2] == inputList[1][1] == inputList[2][0]:
        return inputList[0][2]

    return 'DRAW'


print(whoWin(inputList))

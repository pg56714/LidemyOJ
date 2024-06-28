# 不九人世
# https://oj.lidemy.com/problem/1014
# 在他們的文化裡面，「九」這個數字被視為是不吉利的象徵，是厄運、災禍以及懲罰。
# 因此呢，在他們的數字系統裡面，是沒有 9 這個數字的。所以 8 的下一個數字就是 10，而 18 的下一個數字是 20
# 這個民族叫做「齊」，因此他們把這個數字系統稱作「齊數」，底下是他們的數字系統裡面前 30 個數字：
# 1, 2, 3, 4, 5, 6, 7, 8, 10, 11
# 12, 13, 14, 15, 16, 17, 18, 20, 21, 22
# 23, 24, 25, 26, 27, 28, 30, 31, 32, 33
# 所以從我們的角度來看，在齊數系統當中第 9 個數字是 10，第 21 個數字是 23。
# 現在給你一個齊數系統裡的數字 N，請問這個數字是第幾個數字。

# 輸入為一個數字 N，代表在齊數系統裡的數字

# Sample Input 1
# 33

# Sample Output 1
# 30

# Sample Input 2
# 100

# Sample Output 2
# 81


def find_qin_number_position(N):
    # 方法一 Time Limit Exceeded
    # count = 0
    # current = 0

    # while current < N:
    #     current += 1
    #     if "9" not in str(current):
    #         count += 1

    # return count

    # 方法二 Accepted
    N_str = str(N)
    decimal_value = 0
    power = 0

    for digit in reversed(N_str):
        # print(digit)
        decimal_value += int(digit) * (9**power)
        power += 1

    return decimal_value


N = int(input(""))
print(find_qin_number_position(N))

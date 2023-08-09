# 判斷等差數列

def isValid(arr):
    if (len(arr) <= 1):
        return True

    d = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if (arr[i] - arr[i - 1] != d):
            return False
    return True


print(isValid([1, 3, 5, 7, 9]))
print(isValid([1, 1, 1]))
print(isValid([1, 2, 4]))
print(isValid([]))
print(isValid([1]))

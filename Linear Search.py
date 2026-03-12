def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 23, 45, 70, 11, 15]
target_value = 70
result = linear_search(numbers, target_value)
print(result)
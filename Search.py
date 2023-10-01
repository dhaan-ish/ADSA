def binarySearch(arr, searchElement):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == searchElement:
            return mid
        elif arr[mid] < searchElement:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [2, 9, 11, 14, 17, 21, 46]
targetValue = 17
print("arr =", arr, " Target Value =", targetValue)
result = binarySearch(arr, targetValue)
print("Binary Search by using Divide and Conquer Approach: ", end="")
if result == -1:
    print(targetValue, "is not found.")
else:
    print(targetValue, "is found in index position", result)

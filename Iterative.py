def gcd(a, b):
    GCD = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            GCD = i
    return GCD

def fibonacciSeries(n):
    a, b = -1, 1
    print("The first", n, " terms of fibonacci series : ", end="")
    while n > 0:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        n -= 1

def sequentialSearch(arr, searchElement):
    for i in range(len(arr)):
        if arr[i] == searchElement:
            return i
    return -1

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

print("GCD of 902 and 495 is:", gcd(902, 495))
fibonacciSeries(11)
arr = [2, 9, 11, 14, 17, 21, 46]
searchValue = 17
print("\narr =", arr, " searchValue = ", searchValue)
result = sequentialSearch(arr, searchValue)
print("Sequential Search : ", end="")
if result == -1:
    print(searchValue, "is not found.")
else:
    print(searchValue, "is found in index position", result)
print("Binary Search : ", end="")
result = binarySearch(arr, searchValue)
if result == -1:
    print(searchValue, "is not found.")
else:
    print(searchValue, "is found in index position", result)

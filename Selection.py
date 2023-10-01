import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def selection(arr, k):
    if k < 1 or k > len(arr):
        return None
    return quickselect(arr, 0, len(arr) - 1, k - 1)

arr = [5, 13, 9, 44, 17, 36, 1, 12, 0, -26, 19]
k = 4
answer = selection(arr, k)
if answer is None:
    print("Element does not exist")
else:
    ordinal_suffix = "st" if k == 1 else "nd" if k == 2 else "rd" if k == 3 else "th"
    print("The", str(k) + ordinal_suffix, "smallest element in the given list is:", answer)

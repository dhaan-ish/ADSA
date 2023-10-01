def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr

arr = [45, 90, 17, 4, -21, 84, 101, -3, 0]
ans = bubbleSort(arr.copy())
print("Bubble Sort:", ans)

ans = selectionSort(arr.copy())
print("Selection Sort:", ans)

ans = insertionSort(arr.copy())
print("Insertion Sort:", ans)

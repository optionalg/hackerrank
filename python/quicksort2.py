def print_arr(arr):
    print(" ".join(map(str, arr)))

def quicksort(arr, pivot_i=0):
    if len(arr) <= 1:
        return arr
    pivot = arr[pivot_i]
    left, right = divide(arr, pivot)
    sorted_arr = quicksort(left) + [pivot] + quicksort(right)
    print_arr(sorted_arr)
    return sorted_arr

def divide(arr, pivot):
    left = []
    right = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
    return left, right


n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
quicksort(arr)

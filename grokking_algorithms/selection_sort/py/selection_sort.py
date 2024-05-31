def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):

        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index
    
def selection_sort(arr):
    #This would make copy from original one
    # arr_copy = arr[:]
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

unsorted = [6, 4 , 2, 5, 2 , 1, 5, 12, 2 ,8, 21, 11]
print(selection_sort(unsorted))
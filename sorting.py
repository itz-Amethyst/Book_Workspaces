
def buble_sort(numbers):
    n = len(numbers)
    
    if n <=1:
        return numbers  
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                
    return numbers

def quick_sort(numbers):
    
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle= [x for x in numbers if x == pivot]
    right= [x for x in numbers if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    

unsorted_numbers = [34, 1, 23, 4, 3, 12, 45, 9, 0, 15]

# Using bubbl-sort() function
sorted_numbers_builtin = buble_sort(unsorted_numbers)
print("Sorted numbers using bubble_sort:", sorted_numbers_builtin)

sorted_quick_method = quick_sort(unsorted_numbers)
print("Sorted numbers using quick_sort:", sorted_numbers_builtin)

def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        # IT takes the mid automatically
        mid = (low + high)
        guess = list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            return  mid + 1
        return None
    
my_list = [1,3, 5 , 7 , 9, 11 , 13 , 15]

print(binary_search(my_list, 15))




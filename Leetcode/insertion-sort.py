

def solution(array):

    n = len(array)

    # No sorting to be done
    if n <= 1:
        return array
    
    # iterate over the array, starting from second element
    for i in range(1, n):

        # element to be inserted in sorted order
        key = array[i]

        # Right-most index of the sorted portion of the array
        j = i - 1

        # Move elements over until all elements in sorted portion have been moved or an item less than key is found
        while j >= 0 and key < array[j]:
            array[j+1] = array[j] # Shift element to right
            j -= 1

        array[j + 1] = key # Insert key in the correct position
    
    return array


print(solution([3, 1, 2, 4])) # return [1, 2, 3, 4]
print(solution([12, 11, 13, 5, 6])) # return [5, 6, 11, 12, 13]
print(solution([1])) # return [1]
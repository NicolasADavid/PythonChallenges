def solution(array):
    
    def mergeSort(arr):
        
        if len(arr) <= 1:
            return arr
            
        mid = len(arr)//2
        
        left = arr[:mid]
        right = arr[mid:]
        
        lsorted = mergeSort(left)
        rsorted = mergeSort(right)
        
        return merge(lsorted, rsorted)
        
    def merge(left, right):
        
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        # insert any remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
        
    return mergeSort(array)

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = solution(unsortedArr)
print("Sorted array:", sortedArr)
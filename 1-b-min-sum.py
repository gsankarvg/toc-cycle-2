def min_sum_of_products(arr1, arr2):
    arr1.sort()
    arr2.sort(reverse=True)
    
    min_sum = sum(a * b for a, b in zip(arr1, arr2))
    
    return min_sum

# Example usage:
arr1 = [1, 3, 5, 2]
arr2 = [7, 9, 4, 6]
result = min_sum_of_products(arr1, arr2)
print("Minimum Sum of Products:", result)

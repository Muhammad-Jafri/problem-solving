import copy

def deep_copy(obj):
    return copy.deepcopy(obj)

def shallow_copy(obj):
    return copy.copy(obj)

arr = [[1], [2], [3]]
arr_copy = deep_copy(arr)
# Print the address of the array
print(id(arr))  
print(id(arr_copy))  
arr_copy[0][0] = 100
print(arr) # [100,2,3]
print(arr_copy)  # [100,2,3]

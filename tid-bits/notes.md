# Deep Copy vs Shallow Copy

First you need to know what mutable and immutable elements are.
Mutable elements: lists, dicts, user-defined objects ---> modifies the existing object
Immutable elements: integers, strings and tuples ---> when modifying them, it creates a brand new object

## Shallow Copy
```
import copy
arr = [1,2,3]
s_arr = copy.copy(arr)
s_arr[0] = 100
print(s_arr) # [100,2,3]
print(arr) # [1,2,3] 

arr = [[1], [2], [3]] # Here the sublist is a mutable data structure
arr_copy = shallow_copy(arr)
# Print the address of the array
print(id(arr))  
print(id(arr_copy))  
arr_copy[0][0] = 100
print(arr) # [100,2,3]
print(arr_copy)  # [100,2,3]
```

This is not confusing at all since we modified an immutable object (int) and that's why the changes will not be reflected in the original array

## Deep Copy
doing a deep copy will result in a brand new object and sub objects with totally different memory addresses as well. (consumes more memory)


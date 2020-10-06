def binarySearch(a, low, high, value): 
    if high >= low: 
        mid = (high + low) // 2
        if a[mid] == value: 
            return mid  
        elif a[mid] > value: 
            return binarySearch(a, low, mid - 1, value)  
        else: 
            return binarySearch(a, mid + 1, high, value) 
    else: 
        return -1
  
 
a = [10, 31, 12, 123, 981, 213] 
value_to_search = 123

index = binarySearch(a, 0, len(a)-1, value_to_search) 
  
if index != -1: 
    print("The number " + str(value_to_search) + " is present at index ", str(index)) 
else: 
    print("Number not present") 

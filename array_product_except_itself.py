"""
Given an array arr[] of n integers, construct a Product Array prod[] 
(of the same size) such that prod[i] is equal to the product of all 
+the elements of arr[] except arr[i]. 

Note: Solve it without the division operator in O(n) time.

Example : 

Input: arr[]  = {10, 3, 5, 6, 2}
Output: prod[]  = {180, 600, 360, 300, 900}
3 * 5 * 6 * 2 product of other array 
elements except 10 is 180
10 * 5 * 6 * 2 product of other array 
elements except 3 is 600
10 * 3 * 6 * 2 product of other array 
elements except 5 is 360

10 * 3 * 5 * 2 product of other array 
elements except 6 is 300
10 * 3 * 6 * 5 product of other array 
elements except 2 is 900

"""

#%% Neetcode
from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * (len(nums))
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


#%% test
arr  = [10, 3, 5, 6, 2]
productExceptSelf(nums=arr)


#%% geeksfor geeks
def productArray(arr, n):
    if n==1:
        print(0)
        return
    i, temp = 1, 1
    
    # Allocate memory for the product array
    prod = [1 for i in range(n)]
    
    # initialize the product array as 1
    
    # In this loop, temp variable contains product of
    # elements on left side excluding arr[i]
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]
        
    # Initialize temp to 1 for product on right side
    temp = 1
    
    # In this loop, temp variable contains product of
    # elements on right side excluding arr[i]
    
    for i in range(n-1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]
        
    for i in range(n):
        print(prod[i], end=" ")
        
    return

#%%
# Driver Code
arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is: n")
productArray(arr, n)
        
    
    
         
    
    
    



#%%
nums = 5
for i in range(6-1, -1, -1):
    print(i)

#%%
for i in range(6):
    print(i)










# %%

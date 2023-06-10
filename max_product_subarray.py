"""
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

#%% Neetcode


def maxProduct(nums):
    res = max(nums)
    curMax, curMin = 1, 1
    
    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        tmp = curMax * n
        curMax = max(curMax * n, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

#%% test
nums = [2,3,-2,4]

maxProduct(nums=nums)

#%%
nums = [-2,0,-1]
maxProduct(nums=nums)


#%% geekforgeek
import sys

def maxSubarrayProduct(arr, n):
    ans = -sys.maxsize - 1
    product = 1
    
    for i in range(n):
        product *= arr[i]
        ans = max(ans, product)
        if arr[i] == 0:
            product = 1
            
    product = 1
    
    for i in range(n-1, -1, 1):
        product *= arr[i]
        ans = max(ans, product)
        if arr[i] == 0:
            product = 1
    return ans

#%% test geekforgeek
nums = [2,3,-2,4]
maxSubarrayProduct(nums, n=len(nums))

#%% test geekforgeek



















# %%

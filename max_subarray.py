"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""

#%% Neetcode
from typing import List
def max_sub_array(nums: List[int]) -> int:
    maxSub = nums[0]
    current_sum = 0
    
    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        maxSub = max(maxSub, current_sum)
    return maxSub
        

#%% test 
nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sub_array(nums=nums)

#%% test
nums = [5,4,-1,7,8]
max_sub_array(nums=nums)



#%% geeksforgeeks
from sys import maxsize

def maxSubArray(a, size):
    max_so_far = -maxsize -1
    max_ending_here = 0
    
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

#%% test for geek for geek
nums = [-2,1,-3,4,-1,2,1,-5,4]

maxSubArray(a=nums, size=len(nums))

        
    








# %%

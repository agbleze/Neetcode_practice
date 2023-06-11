"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

#%% neetcode

def majorityElement(nums: list) -> int:
    count = {}
    res, maxCount = 0, 0
    
    for i in nums:
        count[i] = 1 + count.get(i, 0)
        res = i if count[i] > maxCount else res
        maxCount = max(count[i], maxCount)
        
    return res
        

#%% test neetcode

majorityElement(nums = [2,2,1,1,1,1,2])


#%% neetcode 2  space complexity of O(1)

def majorityElement2(nums: list):
    res = 0, 
    count = 0
    for n in nums:
        if count == 0:
            res = n
        count += 1 if res == n else - 1
    return res


#%% test neetcode 2

majorityElement2(nums = [2,2,1,1,1,2,2])
        
    



























# %%

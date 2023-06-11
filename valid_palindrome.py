"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

#%% Neetcode

def isPalindrome(s: str):
    newStr = ""
    
    for c in s:
        if c.isalnum():
            newStr += c.lower()
            
    return newStr == newStr[::-1]
    
#%% test neetcode

isPalindrome(s="A man, a plan, a canal: Panama")

#%% test neetcode
isPalindrome(s = "race a car")

#%% test neetcode
isPalindrome(s = " ")

#%% Neetcode second version

class Solution:
    def isPalindromeV2(self, s: str):
        l, r = 0, len(s) - 1
        
        while l < r:
            while l<r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+ 1, r - 1
        return True            
                
    def alphaNum(self, c):
        self.c = c
        return (ord('A') <= ord(self.c) <= ord('Z') or 
                ord('a') <= ord(self.c) <= ord('z') or 
                ord('1') <= ord(self.c) <= ord('9')
            )
        
        
#%% test 
v2 = Solution()
v2.isPalindromeV2(s="A man, a plan, a canal: Panama")        
                
                
    
                
        









# %%

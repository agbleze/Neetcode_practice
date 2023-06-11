
"""
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
#%%

from typing import Counter
def isAnagram(s: str, t: str):
    return Counter(s) == Counter(t)
    
#%%
isAnagram(s = "anagram", t = "nagaram")    

#%% Neetcode 1

def anagram(s: str, t:str) -> bool:
    counterS = {}
    counterT = {}
    
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        counterS[s[i]] = 1 + counterS.get(s[i], 0)
        counterT[t[i]] = 1 + counterT.get(t[i], 0)
    
    for c in counterS:
        if counterS[c] != counterT[c]:
            return False
        
    return True


#%% test neetcode 2

anagram(s = "anagram", t = "nagaram")
    
#%% Neetcode 2 -- using sorting method

def anagram2(s: str, t: str):
    return sorted(s) == sorted(t)


#%% test neetcode 2
anagram2(s = "anagram", t = "nagaram")

        
        
        













# %%

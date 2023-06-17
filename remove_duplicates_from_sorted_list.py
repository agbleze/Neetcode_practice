"""
Given the head of a sorted linked list, delete all duplicates such that each 
element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

#%% Neetcode

from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next
    return head




#%% test

deleteDuplicates(head = ListNode([1,1,2,3,3]))




# %%

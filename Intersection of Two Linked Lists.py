#Time Complexity: O(len(headA)+len(headB))
#Space Complexity: O(1)
#  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headAlength=0;
        headBlength=0;
        currA=headA;
        while currA:
            currA=currA.next;
            headAlength+=1;
        currB=headB;
        while currB:
            currB=currB.next;
            headBlength+=1;
        while headAlength > headBlength:
            headA=headA.next;
            headAlength-=1;
        while headBlength>headAlength:
            headB=headB.next;
            headBlength-=1;
        currA=headA;
        currB=headB;
        while currA!=currB:
            currA=currA.next;
            currB=currB.next;
        return currA;
            
            
        
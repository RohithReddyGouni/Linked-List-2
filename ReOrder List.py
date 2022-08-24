#Time Complexity: O(n)
#Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
       
        mid=self.Mid(head);
        midnext=mid.next;
        mid.next=None;
        ReverseElementsAfterMid=self.reverse(midnext);
        root=head;
        return self.Merge(root,ReverseElementsAfterMid);
            
    def Merge(self,root,Reverse):
        list1=root;
        list2=Reverse;
        while list2:
            temp=list1.next
            list1.next=list2;
            list2=list2.next;
            list1.next.next=temp;
            list1=temp;
        return list1;
        
        
        
    def Mid(self,head):
        slow=head;
        fast=head;
        while fast.next and fast.next.next:
            slow=slow.next;
            fast=fast.next.next;
        return slow;
    
    def reverse(self,midnext):
        previous=None;
        current=midnext;
        while current:
            nxt=current.next;
            current.next=previous;
            previous=current;
            current=nxt;
        return previous;
        
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        i = 1
        start =curr
        temp =[]
        while curr  and i <=right:
            if i== left:
                start = curr
                print(start.val)
            if i >= left:
                temp.append(curr.val)
            i+=1
            curr=curr.next
        
        temp=temp[::-1]
        print(temp)
        #curr=ListNode(temp[0])
        for i in temp:
            start.val = i
            start = start.next
            
        return head
            
            
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self,list1, list2):
        curr = ListNode(0)
        result = curr
        carry = 0
        sum = 0

        while list1 and list2:
            sum = list1.val + list2.val + carry
            carry = sum // 10
            sum = sum % 10
            list1 = list1.next
            list2 = list2.next
            curr.next = ListNode(sum)
            curr = curr.next
        while list2:
            sum = list2.val + carry
            carry = sum // 10
            sum = sum % 10
            list2= list2.next
            curr.next = ListNode(sum)
            curr = curr.next

        while list1:
            sum = list1.val + carry
            carry = sum // 10
            sum = sum % 10
            list1 = list1.next
            curr.next = ListNode(sum)
            curr = curr.next

       
        if carry != 0:
            curr.next = ListNode(carry)
        return result.next

        

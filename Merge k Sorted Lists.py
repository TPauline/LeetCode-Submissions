# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeKLists(self, lists: List[ListNode]) -> ListNode:
                if lists is None:
                        return None
                lst = []
                for i in lists:
                        if i:
                                curr = i
                                while curr:
                                        lst.append(curr.val)
                                        curr = curr.next
                if not lst:
                        return None
                lst.sort()
                print(lst)
                head =None
                tail = None
                for i in lst:
                        if head is None:
                                head = ListNode(i,None)
                                tail = head
                        else:
                                if tail is None:
                                        head.next = ListNode(i,None)
                                        tail = head.next
                                else:
                                        tail.next =ListNode(i,None)
                                        tail = tail.next
                return head

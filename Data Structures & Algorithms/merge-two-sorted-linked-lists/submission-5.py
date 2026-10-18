# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = curr1
        if not curr1:
            return curr2
        elif not curr2:
            return curr1
        elif not curr1 and not curr2:
            return curr1
        if curr2.val < curr1.val:
            head = curr2
        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next
            if curr1.val <= curr2.val:
                if next1 and next1.val > curr2.val or not next1:
                    curr1.next = curr2
                curr1 = next1
            else:
                if next2 and next2.val >= curr1.val or not next2:
                    curr2.next = curr1
                curr2 = next2
        return head
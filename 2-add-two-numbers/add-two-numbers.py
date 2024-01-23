# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode()
        current = sum_list

        while l1 or l2:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            val_sum = val_l1 + val_l2 + current.val
            current.val = val_sum % 10  # Update the current node's value with the remainder

            # Move to the next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 or l2 or val_sum >= 10:
                current.next = ListNode(val_sum // 10)  
                current = current.next

        return sum_list
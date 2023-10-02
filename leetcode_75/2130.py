# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Firstly, i use two pointer (slow and fast) cycle (1-st while) to find the right middle of the list,
# and as well as inverting the left side of list with new head in the left middle of the initial list.
# Eventually, i get the two linked lists one going from left middle to the start, and second from the 
# right middle to the end (al in terms of initial list).
# At the second cycle 'while' i simply found the max of twins.
# However in this algorithm we encountered with a memory leak, because we change the structure of initial list.
# We can do the reversal again to restore the original list (omitted for simplicity).

class Solution:
    def pairSum(self, head: ListNode | None = None) -> int:
        slow, fast = head, head
        left_part_head = None

        while fast:
            fast = fast.next.next

            left_part_next = slow.next
            slow.next = left_part_head
            left_part_head = slow
            slow = left_part_next

        max_twin_sum = 0
        while slow:
            max_twin_sum = max(max_twin_sum, slow.val + left_part_head.val)
            slow = slow.next
            left_part_head = left_part_head.next
        return max_twin_sum

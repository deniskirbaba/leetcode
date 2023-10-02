# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 1
        # node = head.next
        # while node != None:
        #     length += 1
        #     node = node.next
        # if length == 1:
        #     return None
        # elif length == 2:
        #     head.next = None
        #     return head
        # else:
        #     middle = length // 2
        #     node = head
        #     for i in range(1, middle + 1):
        #         if i == middle:
        #             node.next = node.next.next
        #             break
        #         node = node.next
        #     return head
        if not head.next:
            return None
        step_1 = head
        step_2 = step_1.next.next
        while step_2 and step_2.next:
            step_1 = step_1.next
            step_2 = step_2.next.next
        step_1.next = step_1.next.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not (head and head.next):
        #     return head

        # prev = head
        # cur = prev.next
        # post = cur.next

        # while post:
        #     cur.next = prev
        #     prev = cur
        #     cur = post
        #     post = post.next
        
        # cur.next = prev

        # head.next = None

        # return cur


        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        return new_head
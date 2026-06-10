class Solution:
    def reverseList(self, head: Optional[ListNode], prev = None) -> Optional[ListNode]:
        if head == None:
            return prev

        nxt = head.next
        head.next = prev
        return self.reverseList(nxt, head)
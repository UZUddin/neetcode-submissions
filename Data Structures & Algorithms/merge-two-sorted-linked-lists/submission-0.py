# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode()
        head = sort
        
        #Add least
        while list1 and list2:
            if list1.val < list2.val:
                sort.next = list1
                list1 = list1.next
            else:
                sort.next = list2
                list2 = list2.next
            sort = sort.next

        #Whats left
        if not list1:           
            sort.next = list2
        else:
            sort.next = list1

        head = head.next #remove dummy node
        return head
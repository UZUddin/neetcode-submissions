class ListNode:
    def __init__(self, val: 0, next: None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for x in range(index):
            if curr.next is None:
                return -1
            curr = curr.next
        if curr is None:
            return -1
        return curr.val
            
    def addAtHead(self, val: int) -> None:
        newHead = ListNode(val, None)
        newHead.next = self.head
        self.head = newHead


    def addAtTail(self, val: int) -> None:
        newTail = ListNode(val, None)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = newTail


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            addAtHead(val)
        newNode = ListNode(val, None)
        curr = self.head
        for x in range(index-1):
            if (curr.next is not None):
                curr = curr.next
            elif (curr.next is None) and x<index-1:
                return
        x = curr.next
        curr.next = newNode
        newNode.next = x

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        curr = self.head
        for x in range(index-1):
            if (curr.next is not None):
                curr = curr.next
            elif (curr.next is None) and x<index-1:
                return
        if curr.next is not None:
            x = curr.next.next
            curr.next = x
        else:
            return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
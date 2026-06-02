class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)

        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next

            if not self.head:
                self.tail = None

            return True

        curr = self.head
        i = 0

        while curr and i < index - 1:
            curr = curr.next
            i += 1

        if not curr or not curr.next:
            return False

        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        result = []
        curr = self.head

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result
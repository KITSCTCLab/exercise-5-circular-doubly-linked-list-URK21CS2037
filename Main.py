class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        new_node = Node(data)
        if self.count > 0:
            new_node.previous = self.end
            self.end.next = new_node
            self.head.previous = new_node
            new_node.next = self.head
        else:
            self.head = new_node
        self.end = new_node
        self.count += 1
        return True

    def add_at_head(self, data) -> bool:
        new_node = Node(data)
        if self.count > 0:
            new_node.next = self.head
            new_node.previous = self.end
            self.head.previous = new_node
            self.end.next = new_node
        else:
            self.end = new_node
        self.head = new_node
        self.count += 1
        return True

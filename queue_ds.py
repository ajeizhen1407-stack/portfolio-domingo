class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear:
            self.rear.next = node
        else:
            self.front = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            return None

        node = self.front
        self.front = node.next
        if self.front is None:
            self.rear = None
        node.next = None
        return node.data

    def peek(self):
        return self.front.data if self.front else None

    def to_list(self):
        items = []
        current = self.front
        while current:
            items.append(current.data)
            current = current.next
        return items

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.front = None
        self.rear = None

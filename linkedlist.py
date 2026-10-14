# Lab exercies 3: Linked List - starter file

# Keep every name exactly as written. A renamed class or method counts as a
# missing answer, even if the code inside it is correct.

# Put your own experiments inside the `if __name__ == "__main__":` block at the
# bottom. Code at the top level of this file runs when your work is marked, so
# a stray print() or input() up there will show up in your feedback.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # TODO a: remove the FIRST node and return its data (not the Node).
    # If the list is empty, return None.
    def remove_beginning(self):
        if not self.head:
            return None

        removed_data = self.head.data
        self.head = self.head.next

        # If list became empty after removing the node, update tail
        if self.head is None:
            self.tail = None

        return removed_data

    # TODO b: remove the LAST node and return its data (not the Node).
    # If the list is empty, return None.
    def remove_at_end(self):
        if not self.head:
            return None

        # Case 1: Only one node in the list
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data

        # Case 2: More than one node; traverse to find the second-to-last node
        current = self.head
        while current.next != self.tail:
            current = current.next

        removed_data = self.tail.data
        current.next = None
        self.tail = current
        return removed_data

    # TODO c: remove the first node holding `data` and return its data.
    # If no node holds `data`, return None and leave the list unchanged.
    def remove_at(self, data):
        if not self.head:
            return None

        # Case 1: Target node is at the head
        if self.head.data == data:
            return self.remove_beginning()

        # Case 2: Target node is further down the list
        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                # If removing the tail node, update self.tail
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return removed_data
            current = current.next

        return None

    # TODO d: insert a new node holding `data` right after the first node
    # holding `nodedata`.
    # If no node holds `nodedata`, return None and leave the list unchanged.
    def insert_after(self, nodedata, data):
        current = self.head
        while current:
            if current.data == nodedata:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

                # If inserted after the tail, update self.tail
                if current == self.tail:
                    self.tail = new_node

                return
            current = current.next

        return None


if __name__ == "__main__":
    ll = LinkedList()

    print("--- Inserting 10, 20, 30 ---")
    for value in [10, 20, 30]:
        ll.insert_at_end(value)
    ll.printLinkedList()

    print("\n--- Testing insert_after(20, 25) ---")
    ll.insert_after(20, 25)
    ll.printLinkedList()  # Expected: 10, 20, 25, 30

    print("\n--- Testing remove_at(25) ---")
    print("Removed:", ll.remove_at(25))  # Expected: 25
    ll.printLinkedList()  # Expected: 10, 20, 30

    print("\n--- Testing remove_beginning() ---")
    print("Removed:", ll.remove_beginning())  # Expected: 10
    ll.printLinkedList()  # Expected: 20, 30

    print("\n--- Testing remove_at_end() ---")
    print("Removed:", ll.remove_at_end())  # Expected: 30
    ll.printLinkedList()  # Expected: 20
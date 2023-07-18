# Implement Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return "->".join([str(i) for i in self])

    def __len__(self):
        return sum(1 for _ in self)

    def insert_at_head(self, data):
        return self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        return self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index, data):
        node = Node(data)
        length_list = len(self)

        if not 0 <= index <= length_list:
            raise IndexError("Index is out of range")
        elif self.head is None:
            self.head = self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == length_list:
            temp_pointer = self.head
            while temp_pointer.next:
                temp_pointer = temp_pointer.next
            temp_pointer.next = node
        else:
            pointer = self.head
            for _ in range(0, index - 1):
                pointer = pointer.next
            node.next = pointer.next
            pointer.next = node

    def delete_at_head(self):
        return self.delete_at_nth(0)

    def delete_at_tail(self):
        return self.delete_at_nth(len(self) - 1)

    def delete_at_nth(self, index):
        length_list = len(self)
        delete_node = self.head

        if not 0 <= index <= length_list - 1:
            raise IndexError("Index is not valid")
        elif length_list == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
        else:
            pointer = self.head
            for i in range(0, index):
                if i > 0:
                    pointer = pointer.next
                delete_node = delete_node.next
            pointer.next = delete_node.next
            delete_node.next = None

        return delete_node.data

    def delete(self, data):
        current = self.head
        temp = self.head

        while current.data != data:
            if current.next:
                temp = current
                current = current.next
            else:
                raise ValueError("Data does not exist in list")
        if current == self.head:
            return self.delete_at_head()
        elif current == self.tail:
            return self.delete_at_tail()
        else:
            temp.next = current.next
            current.next = None

    def is_empty(self):
        return len(self) == 0


def test_singly_linked_list():

    test_input = [
        -9,
        100,
        Node(77345112),
        "dlrow olleH",
        7,
        5555,
        0,
        -192.55555,
        "Hello, world!",
        77.9,
        Node(10),
        None,
        None,
        12.20,
    ]
    linked_list = SinglyLinkedList()

    for i in test_input:
        linked_list.insert_at_tail(i)

    # Check if it's empty or not
    assert linked_list.is_empty() is False
    assert (
            str(linked_list) == "-9->100->Node(77345112)->dlrow olleH->7->5555->0->"
                                "-192.55555->Hello, world!->77.9->Node(10)->None->None->12.2"
    )

    # Delete the head
    result = linked_list.delete_at_head()
    assert result == -9
    assert (
            str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
                                "Hello, world!->77.9->Node(10)->None->None->12.2"
    )

    # Delete the tail
    result = linked_list.delete_at_tail()
    assert result == 12.2
    assert (
            str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
                                "Hello, world!->77.9->Node(10)->None->None"
    )

    # Delete a node in specific location in linked list
    result = linked_list.delete_at_nth(10)
    assert result is None
    assert (
            str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
                                "Hello, world!->77.9->Node(10)->None"
    )

    # Add a Node instance to its head
    linked_list.insert_at_head(Node("Hello again, world!"))

    assert (
            str(linked_list)
            == "Node(Hello again, world!)->100->Node(77345112)->dlrow olleH->"
               "7->5555->0->-192.55555->Hello, world!->77.9->Node(10)->None"
    )

    # Add None to its tail
    linked_list.insert_at_tail(None)
    assert (
            str(linked_list)
            == "Node(Hello again, world!)->100->Node(77345112)->dlrow olleH->"
               "7->5555->0->-192.55555->Hello, world!->77.9->Node(10)->None->None"
    )


test_singly_linked_list()


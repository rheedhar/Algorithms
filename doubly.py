# we will need to implement the node class as well as the doubly linked list class.

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    # returns string representation of the node object
    def __str__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # iteration method that helps iterate through the linked list
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    # string representation of the linked list
    def __str__(self):
        return "->".join([str(item) for item in self])

    # return the length of the linked list
    def __len__(self):
        return sum(1 for _ in self)

    # insert node at head of list
    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    # insert node at tail of list
    def insert_at_tail(self, data):
        self.insert_at_nth(len(self), data)

    # insert node at a specified position
    def insert_at_nth(self, index, data):
        length_list = len(self)
        new_node = Node(data)

        if not (0 <= index <= length_list):
            raise IndexError("Index specified is out of range")
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif index == length_list:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            pointer = self.head
            for _ in range(0, index - 1):
                pointer = pointer.next

            temp = pointer.next
            temp.previous = new_node
            new_node.next = temp
            new_node.previous = pointer
            pointer.next = new_node

    # delete node at head of list
    def delete_head(self):
        return self.delete_at_nth(0)

    # delete node at tail of list
    def delete_tail(self):
        return self.delete_at_nth(len(self) - 1)

    # delete node at a specified index
    def delete_at_nth(self, index):
        length_list = len(self)
        delete_node = self.head

        if not (0 <= index <= length_list - 1):
            raise IndexError("Index specified does not exist")
        elif length_list == 1:
            self.head = self.tail = None
        elif index == 0:
            temp = self.head.next
            self.head = temp
            self.head.previous = None
        elif index == length_list - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            delete_node.previous = None
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            delete_node = temp
            delete_node.previous.next = delete_node.next
            delete_node.next.previous = delete_node.previous
        return delete_node.data

    # delete specified data from the linked list
    def delete(self, data):
        current = self.head

        while current.data != data:
            if current.next:
                current = current.next
            else:
                raise ValueError("Data does not exist in linked list")

        if current == self.head:
            return self.delete_head()
        elif current == self.tail:
            return self.delete_tail()
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

    def is_empty(self):
        return len(self) == 0


def test_doubly_linked_list():
    linked_list = DoublyLinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""
    try:
        linked_list.delete_head()
        raise AssertionError
    except IndexError:
        assert True

    try:
        linked_list.delete_tail()
        raise AssertionError
    except IndexError:
        assert True

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_at_nth(i, i + 1)

    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_at_head(0)
    linked_list.insert_at_tail(11)

    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_tail() == 11
    assert linked_list.delete_at_nth(9) == 10

    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))


test_doubly_linked_list()

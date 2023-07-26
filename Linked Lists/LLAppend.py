# We will add the new value in the end, Tail and the value

# but the edge case is when we don't have any value in the list.That is head and tail
# pointed to the node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new = Node(value)
        self.head = new
        self.tail = new
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


my_list = LinkedList(1)
my_list.append(2)

my_list.print_list()

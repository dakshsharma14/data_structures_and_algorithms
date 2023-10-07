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

    # add node to the tail
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # remove the last node
    def pop(self):
        if self.length == 0:
            return None
        #
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        # at this point the pre is pointing to the second last node, and temp at last.
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # after we have decrememtned the list by one
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new = Node(value)
        temp = self.get(index -1)
        new.next = temp.next
        temp.next = new
        self.length +=1
        return True


my_list = LinkedList(0)
my_list.append(2)
my_list.insert(1, 1)

my_list.print_list()

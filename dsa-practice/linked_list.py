class Node:
    """
    An object for storing a single node of a linked list.
    Contains `data` and points to the `next` `Node` in the list, if any.
    """
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    A singly-linked list.
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next
        return ' -> '.join(nodes)

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list in O(n).
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next

        return count

    def search(self, query):
        """
        Searches for the first `Node` containing matching `data` in O(n).
        Returns a `Node` object on match, otherwise `None`.
        """
        current = self.head

        while current != None:
            if current.data == query:
                return current
            current = current.next
        return None

    def prepend(self, data):
        """
        Takes `data`, instantiates it as a new `Node`, and adds it at the head of the list in O(1).
        """
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert(self, data, index):
        """
        Takes `data`, instantiates it as a new `Node`, and adds it at the `index` position in the list in O(n).
        """
        new = Node(data)
        if index == 0:
            return self.prepend(data)

        current = self.head
        count = 0
        while index - 1 > count:
            if current.next == None:
                return "Index out of bounds"
            current = current.next
            count += 1

        # Point new Node to next if any
        if current.next:
            new.next = current.next
        # Point previous Node to new
        current.next = new

    def remove(self, query):
        """
        Removes the `Node` from the list whose `data` matches the `query` in O(n).
        """
        previous = self.head
        current = self.head
        while current != None:
            if current.data == query:
                if current == self.head:
                    self.head = current.next
                previous.next = current.next
                return "Removed %s" % current
            previous = current
            current = current.next
        return "No Node with data %s" % query

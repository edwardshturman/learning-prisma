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
        Searches for the first node containing matching `data`.
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

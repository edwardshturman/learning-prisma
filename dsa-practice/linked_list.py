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


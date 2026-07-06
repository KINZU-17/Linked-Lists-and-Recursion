class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Assign the provided 'data' to an instance variable.
        Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new Node with 'data'.
        Insert it at the front of the list (head).
        Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Create a new Node with 'data'.
        Traverse to the end of the list.
        Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.
        """
        def _sum_helper(node):
            # Base Case: Hit the end of the list
            if node is None:
                return 0
            # Recursive Case: data + sum of the rest of the list
            return node.data + _sum_helper(node.next)
            
        return _sum_helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        """
        def _reverse_helper(current, prev):
            # Base Case: Arrived at the end, 'prev' is now the new head node
            if current is None:
                return prev
            
            next_node = current.next  # Keep track of remaining nodes
            current.next = prev       # Pivot pointer reverse linkage
            
            # Recursive Case: Pass remaining trail forward
            return _reverse_helper(next_node, current)

        self.head = _reverse_helper(self.head, None)

    def recursive_search(self, target):
        """
        Return True if 'target' is found, otherwise False, using recursion.
        """
        def _search_helper(node):
            # Base Case 1: Target value isn't in the list
            if node is None:
                return False
            # Base Case 2: Match confirmed
            if node.data == target:
                return True
            # Recursive Case: Look downstream
            return _search_helper(node.next)

        return _search_helper(self.head)

    def display(self):
        """
        Print the contents of the list for debugging.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append("None")
        print(" -> ".join(elements))
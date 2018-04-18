"""Problem solutions.

1. Implement a function to check if a binary tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node
never differ by more than one.
2. Implement an algorithm to find the kth to last element of a singly linked list.
3. Write a program that outputs all possibilities to put the operators ‘+’, ‘-’, or nothing between
the numbers 1,2,...,9 (in this order) such that the result is 100. For example 1 + 2 + 3 - 4 + 5
+ 6 + 78 + 9 = 100.
"""


"""1. Check if a bst is balanced at every node."""


def is_balanced(root):
    """Check if balanced."""
    return is_balanced_int(root) >= 0


def is_balanced_int(root):
    """Check if balanced."""
    if root is None:
        return 0
    left = is_balanced_int(root.left)
    right = is_balanced_int(root.right)

    if left < 0 or right < 0 or abs(left - right) > 1:
        return -1
    return max((left, right)) + 1


"""2. Implement an algorithm to find the kth to last element of a singly linked list."""


class Node(object):
    """The node object."""

    def __init__(self, data, next):
        """Build node attributes on init."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Create linked list object."""

    def __init__(self, iterable=None):
        """Head node is none on init."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, data):
        """Push value to linked list."""
        if isinstance(data, (tuple, list)):
            for item in data:
                new_node = Node(item, self.head)
                self.head = new_node
                self._counter += 1
        else:
            new_node = Node(data, self.head)
            self.head = new_node
            self._counter += 1

    def pop(self):
        """Remove first item from list and return it."""
        if not self.head:
            raise IndexError("List is empty.")
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def size(self):
        """Return the size of the linked list."""
        return self._counter

    def search(self, val):
        """Search for a node in the linked list."""
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

    def display(self):
        """Display the linked list."""
        output_string = "("
        node = self.head
        if node is None:
            return '()'
        while node:
            try:
                float(node.data)
                output_string += (str(node.data) + ", ")
            except ValueError:
                output_string += ("\'" + node.data + "\'") + ", "
            node = node.next
        output_string = output_string[:-2] + ')'
        return(output_string)

    def __len__(self):
        """Return size of linked list."""
        return self._counter

    def remove(self, node):
        """Remove an item from the linked list."""
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == node:
                if previous_node is None:
                    self.head = current_node.next
                    self._counter -= 1
                    return
                else:
                    previous_node.next = current_node.next
                    self._counter -= 1
                    return
            else:
                previous_node = current_node
                current_node = current_node.next
        raise IndexError('Node not in linked list.')

    def remove_dupes(self):
        """Remove any duplicates in the linked list."""
        if self._counter == 0 or self._counter == 1:
            return
        current_node = self.head
        while current_node:
            next_node = current_node.next
            previous_node = current_node
            while next_node:
                if next_node.data == current_node.data:
                    previous_node.next = next_node.next
                    next_node = next_node.next
                    self._counter -= 1
                    continue
                previous_node = next_node
                next_node = next_node.next
            current_node = current_node.next

    def kth_to_last(self, k):
        """Return the kth to last elements in linked list."""
        if k > self._counter:
            raise IndexError('K greater than length of list.')

        current_node = self.head
        for i in range(k - 1):
            current_node = current_node.next

        kth_to_last_list = []
        while current_node:
            kth_to_last_list.append(current_node.data)
            current_node = current_node.next
        return kth_to_last_list

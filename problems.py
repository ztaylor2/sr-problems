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


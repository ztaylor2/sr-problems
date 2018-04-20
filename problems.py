"""Problem solutions."""

"""Qualitative questions:

1. What are your goals for the next five years?

I am currently very focused on getting my first software engineering job, 
and my hope is that after I get that job I will be able to move 
vertically within that organization. I would like to be something
like a Senior Lead Software Engineer five years from now. 


2. What is your reason for leaving your previous position, 
or why do you want to leave your
current position (if applicable)? 
What do you hope to get out of this position?

The first part of the question is not applicable. 
I hope to gain quality experience and growth as a software engineer. 
I'm seeking a position that will facilitate learning and career growth. 


3. Can you share your biggest professional or academic accomplishment? Can you share
your biggest professional or academic failure?

My biggest academic accomplishment is graduating Cum Laude with a
mechanical engineering degree. This is not an easy thing to do, and I'm 
very proud of the hard work and dedication that accomplishment highlights. 
My biggest professional failure is probably not receiving a job offer 
from the startup Rover. They are currently only hiring senior engineers 
but they decided to give me a chance at the interview process after I 
passed a coding test for them. I then passed an hour long live coding 
phone screen and was assigned a take home coding project. I spent around 
30 hours on the project and ended up not moving forward in the interview 
process. This was fairly discouraging for me, but on the bright side I 
learned a great deal while building out the project and became a 
better software engineer in the process. 

4. What would your peers say are your strengths and weaknesses?

My peers would say my strengths include my work ethic, drive, 
ability to get along with people, and technical aptitude. My weaknesses 
include organization and first impressions. 

"""

"""
Coding Questions: 

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


"""3. Write a program that outputs all possibilities to put the operators ‘+’, ‘-’, or nothing between
the numbers 1,2,...,9 (in this order) such that the result is 100. For example 1 + 2 + 3 - 4 + 5
+ 6 + 78 + 9 = 100."""


def find_all_paths():
    """."""
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    search_sum = 100
    paths = []

    def find_paths(curr_sum, previous_number, index, total_path='1'):
        """."""
        previous_digit = abs(previous_number % 10)

        if index >= len(digits):
            if curr_sum == 100:
                paths.append(total_path)
                return
            return

        current_digit = digits[index]
        concatinated_number = int(str(previous_digit) + str(current_digit))

        if total_path[-2:].isdigit():
            concatinated_path = total_path[:-1] + str(concatinated_number)
        else:
            concatinated_path = total_path + str(concatinated_number)

        find_paths(curr_sum - previous_number, current_digit, index + 1, total_path + ' + ' + str(current_digit))
        find_paths(curr_sum - previous_number, -current_digit, index + 1, total_path + ' - ' + str(current_digit))
        find_paths(curr_sum, concatinated_number, index + 1, concatinated_path)

    find_paths(search_sum, digits[0], 1)

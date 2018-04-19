"""Problem solutions.

1. Implement a function to check if a binary tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node
never differ by more than one.
2. Implement an algorithm to find the kth to last element of a singly linked list.
3. Write a program that outputs all possibilities to put the operators ‘+’, ‘-’, or nothing between
the numbers 1,2,...,9 (in this order) such that the result is 100. For example 1 + 2 + 3 - 4 + 5
+ 6 + 78 + 9 = 100.
"""

"""Qualitative questions."""

"""

1. What are your goals for the next five years?

I am currently very focused on getting my first software engineering job, 
and my hope is that after I get that job I will be able to move 
vertically within that orginization. I would like to be something
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

My biggest academic accomplishmet is graduating Cum Laude with a
mechanical engineering degree. This is not an easy thing to do, and I'm 
very proud of the hard work and dedication that accomplishment highlights. 
My biggest professional failure is probably not recieving a job offer 
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
ability to get along with people, and technical aptitude. My weeknesses 
include organization and first impressions. 

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


"""3. Write a program that outputs all possibilities to put the operators ‘+’, ‘-’, or nothing between
the numbers 1,2,...,9 (in this order) such that the result is 100. For example 1 + 2 + 3 - 4 + 5
+ 6 + 78 + 9 = 100."""


digits = [1,2,3,4,5,6,7,8,9]
searchSum = 100
paths = []


def find_paths(curr_sum, previous_number, index):
    previous_digit = abs(previousNumber % 10)

    # if we are done with the digits
    if index >= len(digits):
        if curr_sum == 100:
            paths.append()

    current_digit = digits[index];
    concatinated_number = int(str(previous_digit) + str(current_digit));

    plus_paths = find_paths(curr_sum-previousNumber, current_digit, index+1);
    minus_paths = find_paths(curr_sum-previousNumber, -current_digit, index+1);
    concat_paths = find_paths(curr_sum, concatinated_number, index+1);


# function concatPrefix(prefix, paths) {
#     return paths
#         .filter(function(p) { return p.length > 0; })
#         .map(function(p) { return prefix.concat(p); });
# }
 
# function findPaths(sum, previousNumber, index) {
#     var previousDigit = Math.abs(previousNumber%10);
#     if (index >= digits.length) {
#         return sum == previousNumber ? [[previousDigit]] : [];
#     }
     
#     var currentDigit = digits[index];
#     var concatenatedNumber = previousNumber >= 0 ? 10*previousNumber + currentDigit : 10*previousNumber - currentDigit;
  
#     var plusPaths = findPaths(sum-previousNumber, currentDigit, index+1);
#     var minusPaths = findPaths(sum-previousNumber, -currentDigit, index+1);
#     var concatPaths = findPaths(sum, concatenatedNumber, index+1);
     
#     var paths = [];
#     Array.prototype.push.apply(paths, concatPrefix([previousDigit, '+'], plusPaths));
#     Array.prototype.push.apply(paths, concatPrefix([previousDigit, '-'], minusPaths));
#     Array.prototype.push.apply(paths, concatPrefix([previousDigit, '&'], concatPaths));
#     return paths;
# }
 
# var foundPaths = findPaths(searchSum, digits[0], 1);
 
# if (foundPaths.length == 0) {
#     console.log("no paths were found");
# } else {
#     for (var i = 0; i < foundPaths.length; i++) {
#         console.log(foundPaths[i].join("").replace(/&/g, ""));
#     }
# }

def get_ones_zeros(size):
    """
    >>> get_ones_zeros(0)
    [[]]
    >>> get_ones_zeros(1)
    [[0], [1]]
    >>> get_ones_zeros(2)
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    >>> get_ones_zeros(3)
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    """
    if size == 0: return [[]]
    else:
        res = get_ones_zeros(size - 1)
        return cons(0, res) + cons(1, res)


def glue(values, glues):
    """
    >>> glue([1,2,3,4,5,6,7,8,9], [0,0,0,0,0,0,0,0,0])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> glue([1,2,3,4,5,6,7,8,9], [1,0,0,0,0,0,0,0,0])
    [12, 3, 4, 5, 6, 7, 8, 9]
    >>> glue([1,2,3,4,5,6,7,8,9], [0,1,0,0,0,0,0,0,0])
    [1, 23, 4, 5, 6, 7, 8, 9]
    >>> glue([1,2,3,4,5,6,7,8,9], [0,1,1,1,1,1,1,1,1])
    [1, 23456789]
    """
    
    index_j = 0
    index_i = 0
    size = len(values)
    
    result = []
    value_stack = values[0]
    
    while index_i < size:
        
        # the case over the boundary
        if index_i + 1 >= size:
            result.append(value_stack)
            break
        
        new_value = values[index_i + 1]
        # normal case
        if glues[index_j] == 0:
            result.append(value_stack)
            value_stack = new_value
        else:
            value_stack = value_stack * 10 + new_value
                
        index_i += 1
        index_j += 1

    return result


def get_numbers(stop = 9):
    """returns all the possible numbers combined from 1 to 9."""
    values = range(1, stop+1)
    one_zeros = get_ones_zeros(stop)
    result = []
    for one_zero in one_zeros:
        res = glue(values, one_zero)
        # list cannot be a member of a set, so the result should be turn into a tuple
        result.append(tuple(res))
    return set(result)
    
def solution(stop = 9, goal = 100):
    """."""
    numbers = get_numbers(stop)
    for number in numbers:
        variations = map(lambda y: [number[0]] + y, random_values(number[1:]))
        for v in variations:
            summed_value = sum(v)
            if goal == summed_value:
                print(v)
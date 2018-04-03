class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next
    # Add insert method here

    def insert(self, head, data):
        """ Insert a node at the end of the given LL. """
        new_node = Node(data)
        if head is None:
            head = new_node
            return head
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
            return head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)

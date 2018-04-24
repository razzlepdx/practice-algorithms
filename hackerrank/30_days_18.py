import sys


class Solution:
    # Write your code here

    def __init__(self):
        """ Instantiates a Solution object. """
        self.queue = []
        self.stack = []

    def pushCharacter(self, char):
        """ Pushes character onto stack instace attribute. """

        self.stack.append(char)

    def enqueueCharacter(self, char):
        """ Enqueues a character onto the queue instance attribute. """

        self.queue.append(char)

    def popCharacter(self):
        """ Pops and returns the character at the top of the stack. """

        return self.stack.pop()

    def dequeueCharacter(self):
        """ Dequeues and returns the first item in the queue. """

        return self.queue.pop(0)

# read the string s
s = raw_input()
#Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''

for i in range(l / 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write("The word, "+s+", is not a palindrome.")

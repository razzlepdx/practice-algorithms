# Mock Interviews at Jet Reports
# 5/16/2018

# q1: Write a function determines if all characters in a string are unique

# input: string
# output: boolean

def is_unique(strng):

    return len(set(strng)) == len(strng)

# another possible solution: iterate over string, assign each character to a
# dictionary, if char is already in dict, fail fast

#===========================

# q2: FizzBuzz variation:  Implement a version of FizzBuzz that takes in a list
# of strings.  If a word in the list contains the letter A, print Fizz, if it
# contains the letter B, print Buzz, and if it contains both, print BuzzBuzz.

# input: list of strings
# output: print statements only

def new_FizzBuzz(lst):

    for word in lst:
        if "a" in word.lower() and "b" in word.lower():
            print "BuzzBuzz"
        elif "a" in word.lower():
            print "Fizz"
        elif "b" in word.lower():
            print "Buzz"

if __name__ == "__main__":
    print is_unique("1234")
    print "^ should be true"
    print is_unique("hello")
    print "^ should be false"
    print new_FizzBuzz(["baby", "butter", "wall"])
    print "should be: \nBuzzBuzz\nBuzz\nFizz"

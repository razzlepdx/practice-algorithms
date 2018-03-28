# Enter your code here. Read input from STDIN. Print output to STDOUT


def odds_and_evens(string):
    """ Takes in a single string as an argument and returns another string containing all
    letters at even indexes (a) and all letters at odd indexes (b) in
    the following pattern: 'a b' """

    odds = ''
    evens = ''

    for i, char in enumerate(string):
        if i == 0 or i % 2 == 0:
            evens += char
        else:
            odds += char
    return evens + " " + odds

# handle STDIN and print results to STDOUT

num_strings = int(raw_input())
while num_strings:
    print odds_and_evens(raw_input())
    num_strings -= 1

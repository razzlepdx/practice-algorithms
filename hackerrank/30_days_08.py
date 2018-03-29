# Enter your code here. Read input from STDIN. Print output to STDOUT

# create phone book dictionary with known number of inputs
num_entries = int(raw_input())
phone_book = {}
while num_entries:
    name, number = raw_input().rstrip().split(" ")
    phone_book[name] = number
    num_entries -= 1


def get_phone_numbers(name, phone_book):
    """ Takes in a phone book and name to search, and returns a string representing
    the result, or an error message stating that the number could not be found."""

    if phone_book.get(name):
        return name + "=" + phone_book[name]

    return "Not found"

# handle unknown number of phone_book queries and print the results
while True:
    try:
        print get_phone_numbers(raw_input(), phone_book)
    except:
        break

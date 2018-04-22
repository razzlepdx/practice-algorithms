'''
QUESTION: Given a string as your input, delete any reoccurring character,
and return the new string.
'''

# strategy 1 - iterate over string, utilize dictionary


def delete_repeat_chars(phrase):
    """ Given a string, returns a new string that contains only the first
    occurance of each letter. """
    final_str = ''
    letters = {}

    for char in phrase:

        if letters.get(char):  # if already in dict, move on to next letter
            continue
        # otherwise, add char to dictionary and append to final_str
        letters[char] = True
        final_str += char

    return final_str

print(delete_repeat_chars("aabbcc"))
#-------------------------------------------
# optimization - use set instead of dictionary, since value is not pertinent


def del_repeat_chars(phrase):
    """ Given a string, returns a new string that contains only the first
    occurance of each letter. """

    final_str = ''
    letters = set()

    for char in phrase:
        if char not in letters:
            letters.add(char)
            final_str += char

    return final_str

print(del_repeat_chars("aabbcc"))
#------------------------------------------
# strategy 2 - split string, setify, and rejoin to return new string


def del_repeat_letters(phrase):
    """ Given a string, returns a new strings that contains only one
    occurance of each letter. """

    final = set(list(phrase))
    return "".join(final)

print(del_repeat_letters("aabbccdd"))

# cons: does not maintain order, no memory benefit

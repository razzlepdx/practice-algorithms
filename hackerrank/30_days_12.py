# solution for day 12 of Hackerrank 30 days of Code challenge

class Student(Person):

    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        """ Creates a new instance of the Student class. """

        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        """ Calculates the average score for a studen and returns grade. """

        num_scores = len(self.scores)
        total = sum(self.scores)
        grade = int(total / num_scores)

        if grade >= 90:
            return "O"
        elif grade >= 80:
            return "E"
        elif grade >= 70:
            return "A"
        elif grade >= 55:
            return "P"
        elif grade >= 40:
            return "D"
        else:
            return "T"

#Write your code here


class Calculator:

    def power(self, first, second):

        if first >= 0 and second >= 0:
            return first ** second

        return "n and p should be non-negative"

myCalculator = Calculator()

T = int(raw_input())

for i in range(T):
    n, p = map(int, raw_input().split())
    try:
        ans = myCalculator.power(n, p)
        print ans
    except Exception, e:
        print e

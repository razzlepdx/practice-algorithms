class Difference:

    def __init__(self, a):
        self.__elements = a
        # Add your code here

    def computeDifference(self):
        """ Given a list of non-negative numbers, assigns the value of the
        maximum difference to self.maximumDifference."""

        max_diff = 0
        nums = self.__elements
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                diff = abs(nums[i] - nums[j])
                if diff > max_diff:
                    max_diff = diff

        self.maximumDifference = max_diff
# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference

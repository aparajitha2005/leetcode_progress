class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        prev = 0

        for i in s:
            if roman[i] > prev:
                curr = roman[i]
                total = total + curr - (2 * prev)

            else:
                curr = roman[i]
                total = total + curr

            prev = roman[i]

        return total
        """
        :type s: str
        :rtype: int
        """
        
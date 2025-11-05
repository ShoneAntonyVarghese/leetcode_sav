class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = {
           'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev = 0

        for i in s[::-1]:
            value = l[i]

            if value < prev:
                result -= value
            else:
                result += value
                prev = value

    
        return result
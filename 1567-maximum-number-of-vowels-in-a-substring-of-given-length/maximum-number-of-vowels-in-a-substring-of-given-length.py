class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        old_v = list(s[:k])
        vowels = "aeiou"
        

        count = 0
        i = 0
        while i != k:
            if old_v[i] in vowels:
                count += 1
            i += 1
        
        max_count = count  

        for r in range(k, len(s)):
            if old_v[0] in vowels: 
                count -= 1
            old_v.pop(0)

            old_v.append(s[r])
            if s[r] in vowels:     
                count += 1

            if count > max_count:
                max_count = count

        return max_count

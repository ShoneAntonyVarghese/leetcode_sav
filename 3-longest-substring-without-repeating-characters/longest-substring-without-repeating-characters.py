class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = []    
        left = 0              
        max_len = 0           

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1     

            seen.append(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

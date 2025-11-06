class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        
        # Sum of the first window
        window_sum = sum(arr[:k])
        
        # Check first window
        if window_sum // k >= threshold:
            count += 1
        
        # Slide the window
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i-k]   # Add new, remove old
            if window_sum // k >= threshold:
                count += 1
        
        return count

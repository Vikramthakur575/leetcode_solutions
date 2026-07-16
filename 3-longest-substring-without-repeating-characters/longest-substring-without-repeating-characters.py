class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Stores all unique characters currently in the window
        seen = set()

        # Left pointer of the sliding window
        left = 0

        # Stores the maximum length found so far
        max_length = 0

        # Right pointer moves through the string
        for right in range(len(s)):

            # If current character already exists in the window,
            # shrink the window from the left until it becomes unique
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character to the window
            seen.add(s[right])

            # Update the maximum window size
            max_length = max(max_length, right - left + 1)

        # Return the longest substring length
        return max_length
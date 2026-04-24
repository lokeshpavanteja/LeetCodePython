class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            current = s[right]

            # If duplicate found, move left pointer
            if current in char_map:
                left = max(left, char_map[current] + 1)

            # Update last seen index
            char_map[current] = right

            # Update max length
            max_length = max(max_length, right - left + 1)

        return max_length


# Example run
s = "pwwkew"
sol = Solution()
print("Input:", s)
print("Output:", sol.lengthOfLongestSubstring(s))
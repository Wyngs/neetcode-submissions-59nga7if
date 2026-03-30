class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_to_next = {}

        i = 0
        ans = 0

        for x in range(len(s)):
            if s[x] in char_to_next:
                i = max(i, char_to_next[s[x]])

            ans = max(ans, x-i+1)

            char_to_next[s[x]]= x+1

        return ans

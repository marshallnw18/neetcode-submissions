class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store the maximum length
        charSet = set()
        leftPointer = 0
        result = 0

        for rightPointer in range(len(s)):
            # if rightPointer is in the charSet
            while s[rightPointer] in charSet:
                charSet.remove(s[leftPointer])
                leftPointer += 1
            # if rightPoiner is not in the charSet
            charSet.add(s[rightPointer])
            result = max(result, rightPointer - leftPointer + 1)
        
        return result
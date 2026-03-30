import pprint 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = 1
            else:
                return True

        
        pprint.pprint(hashmap)
        return False 
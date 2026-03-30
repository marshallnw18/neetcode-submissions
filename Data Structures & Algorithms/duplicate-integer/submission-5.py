class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap:
                print("In the map")
                return True
            else:
                print("Adding to map..")
                hashmap[num] = "Encountered"
        
        return False

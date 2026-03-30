class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_arr = sorted(nums)
        
        for i in range(len(sorted_arr) - 1):
            if sorted_arr[i] == sorted_arr[i+1]:
                return True 

        return False

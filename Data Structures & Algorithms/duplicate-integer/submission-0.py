class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_numbers = sorted(nums)

        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] == sorted_numbers[i - 1]:
                return True
            elif sorted_numbers[i] == sorted_numbers[i + 1]:
                return True
        
        return False
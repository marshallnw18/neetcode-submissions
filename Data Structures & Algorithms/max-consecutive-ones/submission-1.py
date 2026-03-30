class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_consecutive_count = 0
        largest_consecutive = 0
    
        for i in range(len(nums)):
            if nums[i] == 1:
                current_consecutive_count += 1
                print(f"Value: {nums[i]}, Count: {current_consecutive_count}")
            elif nums[i] == 0:
                if current_consecutive_count > largest_consecutive:
                        largest_consecutive = current_consecutive_count
                current_consecutive_count = 0
                print(f"Value: {nums[i]}, Count Reset: {current_consecutive_count}")

        if current_consecutive_count > largest_consecutive:
            largest_consecutive = current_consecutive_count
        return largest_consecutive
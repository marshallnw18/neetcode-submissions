class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            occurrence = nums.index(val)
            nums.pop(occurrence)

        k = len(nums)

        return k
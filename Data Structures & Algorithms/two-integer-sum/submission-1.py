class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        return_vals = []

        for i, num in enumerate(nums):
            value_we_want = target - num
            if value_we_want in hashmap:
                return_vals.append(hashmap[value_we_want])
                return_vals.append(i)
            else:
                hashmap[num] = i
        return return_vals
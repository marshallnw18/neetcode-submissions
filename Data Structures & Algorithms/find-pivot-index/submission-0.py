class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # initializes an empty list of zeros
        prefixSum = [0] * (n + 1)

        # calculates the prefix sums 
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
            print("Left: ", prefixSum[i + 1])

        for i in range(n):
            leftSum = prefixSum[i]
            rightSum = prefixSum[n] - prefixSum[i + 1]
            if leftSum == rightSum:
                return i 
                
        return -1
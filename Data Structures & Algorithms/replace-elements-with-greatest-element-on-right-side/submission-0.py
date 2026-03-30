class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrLength = len(arr)

        returnList = [0] * arrLength

        for currentIndex in range(arrLength):
            rightMax = -1
            for trailingValue in range(currentIndex + 1, arrLength):
                # Determine the max between -1 and the trailing value
                rightMax = max(rightMax, arr[trailingValue])
            returnList[currentIndex] = rightMax

        return returnList
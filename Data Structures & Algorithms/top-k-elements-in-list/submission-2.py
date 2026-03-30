import pprint
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        returnList = []

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                # print("Key..", nums[i])
                # print("Value: ", hashmap[nums[i]])
            else:
                # print("Key..", nums[i])
                # print("Updates to..", str(hashmap[nums[i]] + 1))
                hashmap[nums[i]] += 1

        #pprint.pprint(hashmap)

        for i in range(k):
            #print("Current max value is.. ", max(hashmap, key=hashmap.get))
            returnList.append(max(hashmap, key=hashmap.get))
            hashmap.pop(max(hashmap, key=hashmap.get))

        return returnList
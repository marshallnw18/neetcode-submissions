import pprint
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        # enumerate the list to get index and values
        for i, num in enumerate(nums):
            potential_duplicate = num

            if potential_duplicate in hashmap:
                print("Duplicate found!")
                pprint.pprint(hashmap)
                return True
            else:
                print("Adding non-duplicate to hashmap..")
                hashmap[potential_duplicate] = "Already Seen"
        
        print("No duplicates found in list!")
        pprint.pprint(hashmap)
        return False
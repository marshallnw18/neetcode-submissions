import pprint
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first determine which words are anagrams of the current one
        # store all words in a hashmap with their sorted values
        hashmap = {}
        returnList = []

        # adds everything to a hashmap
        for inputStr in strs:

            sortedStr = sorted(inputStr)
            formatted_str = ", ".join(sortedStr)

            if formatted_str not in hashmap:
                print("Adding to map...")
                hashmap[formatted_str] = [inputStr]
            elif formatted_str in hashmap:
                print("Adding new word to anagram match..")
                hashmap[formatted_str].append(inputStr)  

        pprint.pprint(hashmap)
        
        # iterate over the hashmap and output the sublists 
        for key in hashmap:
            returnList.append(hashmap[key])

        return returnList
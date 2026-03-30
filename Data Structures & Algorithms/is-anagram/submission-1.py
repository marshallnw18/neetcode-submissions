class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = sorted(s)
        arrT = sorted(t)

        if arrS == arrT:
            return True
        else:
            return False 
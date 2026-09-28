class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        set1 = set()
        set2 = set()

        set1 = sorted(s)
        set2 = sorted(t)
        
        return set1 == set2
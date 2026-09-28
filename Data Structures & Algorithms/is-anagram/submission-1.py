class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        #both same len so doesnt matter if its len(s) or len(t)
        for i in range(len(s)):
            # increase character count by 1 for each instance of char in the string
            countS[s[i]] = 1 + countS.get(s[i], 0) # < -- default to count 0 if it isnt in the map
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # now loop thru the maps and check that each key has the same # of counts for the value

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True


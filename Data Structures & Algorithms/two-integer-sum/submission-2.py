class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #one pass using hashmap - find the diff between the target and the current num, then check if that diff is in the hashmap. if it is, the answer is that num in the map and the current index of the arr that you checked. if not, add curr num to hashmap and keep iterating thru the list.

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        

    

        

        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #map with value and index of value
        # Check the diff between the target and each val in the array. Then check if that diff is 
        # in the hashmap. If it is, return the index of the current val and the index of the val in the map
        hashMap = {} # val: index


        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[nums[i]] = i




        
        
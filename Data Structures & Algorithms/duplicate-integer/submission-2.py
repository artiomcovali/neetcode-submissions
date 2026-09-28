class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        countMap = {}
        ans = False

        for i in range(len(nums)):
            if nums[i] in countMap:
                ans = True
            else:
                countMap[nums[i]] = i
        return ans
         
        
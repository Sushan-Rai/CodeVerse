class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = i
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if (dict1.get(diff) is not None) and (dict1[diff] != i):
                res = [i,dict1[diff]]
        return res
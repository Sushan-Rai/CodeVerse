class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)
        maxcount = 0
        for i in setNum:
            if i-1 not in setNum:
                count = 1
                while i+1 in setNum:
                    count+=1
                    i+=1
                maxcount = max(maxcount,count)
        return maxcount
        
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeroptr = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[i],nums[zeroptr] = nums[zeroptr],nums[i]
                zeroptr+=1
            i+=1
        oneptr = zeroptr
        j = zeroptr
        while j < len(nums):
            if nums[j] == 1:
                nums[j],nums[oneptr] = nums[oneptr],nums[j]
                oneptr+=1
            j+=1
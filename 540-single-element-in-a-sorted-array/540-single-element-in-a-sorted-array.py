
class Solution(object):
    def singleNonDuplicate(self, nums):
        for i in range(0,len(nums)-2,2):
            if nums[i]!=nums[i+1]:
                return nums[i]
        return nums[-1]
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
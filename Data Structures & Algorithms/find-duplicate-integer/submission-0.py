class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=0
        for i in range(len(nums)+1):
            if nums[x]==0:
                return x
            temp=nums[x]
            nums[x]=0
            x=temp
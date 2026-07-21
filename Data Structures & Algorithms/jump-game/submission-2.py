class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        nums=nums[::-1]
        R=1
        L=0
        while R<len(nums):
            if nums[R]>0 and R-L<=nums[R]:
                L=L+nums[R]
                R=L+1
            else:
                R+=1
            if L>=len(nums)-1:
                return True

        return False
            
                
        
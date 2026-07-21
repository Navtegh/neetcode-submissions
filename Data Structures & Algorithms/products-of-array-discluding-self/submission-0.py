class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        result=[1]*n
        curr=1
        for i in range(len(nums)):
            curr=curr*nums[i]
            prefix[i]=curr
        curr=1
        for i in range(len(nums)-1,-1,-1):
            curr=curr*nums[i]
            suffix[i]=curr
        for i in range(len(nums)):
            result[i]=(prefix[i-1] if i-1>=0 else 1)* (suffix[i+1] if i+1<n else 1)
        return result
        
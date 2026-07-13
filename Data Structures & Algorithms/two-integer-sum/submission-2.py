class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums) ):
                if nums[i]+nums[j]==target:
                    if i<j:
                        return [i,j]
                    else:
                        return [j,i]
                else:
                    continue                
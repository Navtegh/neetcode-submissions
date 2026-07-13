class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=set()
        for i in range(len(nums)):
            if nums[i] not in x:
                x.add(nums[i])
            else:
                return True
        return False
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        mid=int((high+low)/2)
        while low<=high:
            print(nums[mid])
            if nums[mid]>target:
                high=mid-1
                mid=int((high+low)/2)
            elif nums[mid]<target:
                low=mid+1
                mid=int((high+low)/2)
            elif nums[mid]==target:
                return mid
        return -1
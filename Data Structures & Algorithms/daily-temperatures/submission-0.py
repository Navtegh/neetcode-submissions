class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr= len(temperatures)*[0]
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
               stackT, stackInd = stack.pop()     
               arr[stackInd] = i - stackInd
            stack.append((t, i))
        return arr

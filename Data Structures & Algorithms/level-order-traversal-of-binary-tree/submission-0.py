# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        x=deque()
        if root:
            x.append(root)
        res=[]
        while len(x)>0:
            level=[]
            for i in range(len(x)):
                curr=x.popleft()
                level.append(curr.val)
                if curr.left:
                    x.append(curr.left)
                if curr.right:
                    x.append(curr.right)
            res.append(level)
        return res

            
        


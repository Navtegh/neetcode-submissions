# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        x= deque()
        if root:
            x.append(root)
        res=[]
        last=None
        while len(x)>0:
            for i in range(len(x)):
                curr=x.popleft()
                last=curr.val
                if curr.left:
                    x.append(curr.left)
                if curr.right:
                    x.append(curr.right)
            res.append(last)
        return res
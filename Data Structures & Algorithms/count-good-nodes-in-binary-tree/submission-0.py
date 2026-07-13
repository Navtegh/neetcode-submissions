# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(root,maxi):
            if not root:
                return None
            nonlocal res
            maxi=max(maxi, root.val)
            if root.val>=maxi:
                res+=1
            left=dfs(root.left,maxi)
            right=dfs(root.right,maxi)

        dfs(root,-101)
        return res
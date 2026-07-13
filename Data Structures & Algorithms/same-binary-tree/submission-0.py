# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        issame=True
        def dfs(root1, root2):
            nonlocal issame
            if not root1 or not root2:
                if root1:
                    issame=False
                if root2:
                    issame=False
                return None
            
            if root1.val!=root2.val:
                issame=False
            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)
        dfs(p,q)
        return issame
        

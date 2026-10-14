# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # augmented tree 
        # self.val = val
        # dfs
        # helper returns [depth, balanced?] for each node as we dfs down 
        def helper(root):
            if not root:
                return 0, True 
            left_depth, left_bal = helper(root.left)
            right_depth, right_bal = helper(root.right)
            res =  abs(left_depth-right_depth)<=1 and left_bal and right_bal 
            height = max(left_depth, right_depth) + 1
            return height, res  
        depth, res = helper(root)
        return res 


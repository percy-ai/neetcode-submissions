# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # append longest depth to each node (augmented tree)
        # longest path = left depth + right depth + 1
        # go down the tree, check for the longest depth 
        if not root:
            return 0 
        if not root.left and not root.right:
            return 0 
        res = 0 
        def depth(root): 
            nonlocal res 
            if not root:
                return 0 
            left = depth(root.left)
            right = depth(root.right)
            curr = left + right 
            res = max(curr, res)
            return max(left,right) + 1 
        
        depth(root)
        return res 



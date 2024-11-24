# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Base case: if root is None or root is one of the nodes (p or q), return root
        if not root or root == p or root == q:
            return root

        # Search for LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in both subtrees, root is their LCA
        if left and right:
            return root

        # Otherwise, return the non-None result from left or right
        return left if left else right
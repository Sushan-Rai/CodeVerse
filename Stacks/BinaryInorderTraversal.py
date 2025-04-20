class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def inorder(root):
            if root == None:
                return []
            
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
            return result
        inorder(root)
        return result
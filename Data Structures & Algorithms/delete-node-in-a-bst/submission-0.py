# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)
        elif root.val == key:
            #case 0 children
            if not root.left and not root.right:
                return 
            #case 1 child
            elif root.left and not root.right:
                root = root.left
                return root
            elif root.right and not root.left:
                root = root.right
                return root
            #case 2 children
            else:
                #helper method to find smallest 
                x = self.findSmallest(root.right) 
                root.val = x.val
                #delete x. new right tree
                root.right = self.deleteNode(root.right, x.val)
                return root
        return root
    def findSmallest(self, root):
        while root.left:
            root = root.left
        return root
       

            

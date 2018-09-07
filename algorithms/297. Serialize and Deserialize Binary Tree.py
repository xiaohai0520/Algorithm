# use preorder into array to str
# build tree from preorder use array

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        stack,res = [root],[]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(str(cur.val))
            else:
                res.append('None')
            if cur:
                stack.append(cur.right)  
                stack.append(cur.left)
        re = ','.join(res)
        return re
                     

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # if not data:
        #     return None
        data = data.split(',')
        data.reverse()
        return self.helper(data)
        
        
    def helper(self,data):
        if not data:
            return None
        cur = data.pop()
        if cur == 'None':
            return None
        root = TreeNode(int(cur))
        root.left = self.helper(data)
        root.right = self.helper(data)
        
        return root
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

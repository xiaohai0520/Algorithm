# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        # stack = [TreeNode(pre[0])]
        # j = 0
        # for v in pre[1:]:
        #     node = TreeNode(v)
        #     while stack[-1].val == post[j]:
        #         stack.pop()
        #         j += 1
        #     if not stack[-1].left:
        #         stack[-1].left = node
        #     else:
        #         stack[-1].right = node
        #     stack.append(node)
        # return stack[0]
        if not pre or not post: return None
        root = TreeNode(pre[0])
        if len(post) == 1: return root
        idx = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1: idx], post[:(idx - 1)])
        root.right = self.constructFromPrePost(pre[idx: ], post[(idx - 1):-1])
        return root
    
    
    
    

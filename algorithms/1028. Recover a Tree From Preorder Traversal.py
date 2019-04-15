This is a pre order tree problem.

The root is always the first one. '-' means the level.

We maintain a stack and each time if the level increase, we add new node in and make the node as the child of the stack[-1]

if the level < len(stack), we need to pop extra node and find the match node.

at last,return the first one of the stack.

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        index = 0
        while index < len(S):
            level = 0
            val = ''
            while index < len(S) and S[index] == '-':
                level += 1
                index += 1
            while index < len(S) and S[index] != '-':
                val += S[index]
                index += 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(int(val))
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

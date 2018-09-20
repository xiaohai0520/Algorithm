#bfs


class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [(root,0,0)]
        cur_depth = left = ans = 0
        while queue:
            cur,depth,pos = queue.pop(0)
            if cur.left:
                queue.append((cur.left,depth+1,2*pos))
            if cur.right:
                queue.append((cur.right,depth+1,2*pos+1))
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1,ans)
        return ans

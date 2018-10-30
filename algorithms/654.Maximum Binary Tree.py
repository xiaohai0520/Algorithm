class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxid = 0
        maxvalue = float("-inf")
        for i,num in enumerate(nums):
            if num > maxvalue:
                maxvalue,maxid = num,i
        root = TreeNode(maxvalue)
        root.left = self.constructMaximumBinaryTree(nums[:maxid])
        root.right = self.constructMaximumBinaryTree(nums[maxid+1:])
        return root

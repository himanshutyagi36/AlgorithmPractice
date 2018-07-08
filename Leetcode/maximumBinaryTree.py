## https://leetcode.com/problems/maximum-binary-tree/description/
class Solution:
    def findMaxNumber(self,nums):
        maxVal = nums[0]
        maxIndex = 0
        for i in range(1,len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxIndex = i
        return maxVal,maxIndex
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        maxVal,maxIndex = self.findMaxNumber(nums)
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        return root
        

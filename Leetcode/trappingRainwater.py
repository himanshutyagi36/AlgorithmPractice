## DP solultion
## keep track of teh max height in left and right array for any index i
## add the difference of min(leftMaax,rightMax) - height[i]
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        ans = 0
        leftMax = [0]*n
        rightMax = [0]*n
        leftMax[0] = height[0]
        for i in range(1,n):
            leftMax[i] = max(height[i], leftMax[i-1])
        rightMax[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i] = max(height[i], rightMax[i+1])
            
        for i in range(n):
            ans += min(leftMax[i], rightMax[i]) - height[i];
        return ans

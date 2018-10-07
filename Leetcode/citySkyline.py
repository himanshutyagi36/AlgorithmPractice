## https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
class Solution:
    
    def findMaxInCol(self,grid,m,n):
        ret = [0]*n
        for j in range(n):
            i=1
            temp = grid[0][j]
            while i<m:
                if grid[i][j] > temp:
                    temp = grid[i][j]
                i+=1
            ret[j] = temp
        return ret
    
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        maxSum = 0
        maxInCol = self.findMaxInCol(grid,m,n)
        for i in range(m):
            maxInRow = max(grid[i])          
            for j in range(n):
                currValue = maxInRow if maxInRow < maxInCol[j] else maxInCol[j]
                maxSum+= abs(currValue - grid[i][j])
        return maxSum
                

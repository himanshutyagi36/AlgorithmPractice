## https://leetcode.com/problems/flipping-an-image/description/
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(A)
        for i in range(length):
            current = A[i]
            start = 0
            end = len(current)-1
            while start<end:
                current[start],current[end] = current[end],current[start]
                start+=1
                end-=1
        for i in range(length):
            B = A[i]
            for j in range(len(B)):
                B[j]^=1
                
        return A
        
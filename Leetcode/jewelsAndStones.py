## https://leetcode.com/problems/jewels-and-stones/description/
from collections import defaultdict
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = defaultdict(int)
        for c in J:
            d[c] +=1
        ret = 0
        for c in S:
            if c in d:
                ret+=1
        return ret
        

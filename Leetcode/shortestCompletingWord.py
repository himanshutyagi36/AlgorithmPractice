## https://leetcode.com/problems/shortest-completing-word/description/
import collections
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        ## idea is to iterate through licensePlate and add the number of occurances 
        ## of each letter in dictionary. Then iterate through all the words, and 
        ## update the answer according to the length of the smallest word that 
        ## contains all the letter from licence plate.
        ans = ""
        d = collections.defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                d[c.lower()] += 1
        for w in words:
            for k, v in d.items():
                if w.count(k) < v:
                    break
            else:
                if not ans:
                    ans = w
                elif len(w) < len(ans):
                    ans = w
        return ans

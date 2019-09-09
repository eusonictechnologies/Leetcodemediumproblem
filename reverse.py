#There are two steps:

#1. use the space ‘ ‘ to determine the boundary of words. We reverse each subarray separated by space. 
#2.  reverse the whole array.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split() #split the string, it automatically puts it in a list
        res = "" #initialize space
        for i in range(len(s)): #for every element in the string list
            res = s[i]+ " " +res #reverse the string word by word. A word is defined as a sequence  of non-space characters.
        return res[:-1]
    
#Time Complexity: O(n)

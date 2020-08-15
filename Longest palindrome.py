class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter=[]
        for i in s:
            if i in counter:
                counter.remove(i)
            else:
                counter.append(i)
        if counter:
            return len(s)-(len(counter)-1)
        else:
            return len(s)

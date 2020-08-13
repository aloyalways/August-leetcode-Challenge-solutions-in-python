class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        n=len(s)-1
        ans=0
        for i in s:
            index=alphabets.index(i)+1
            ans+=(26**n)*index
            n-=1
        return ans

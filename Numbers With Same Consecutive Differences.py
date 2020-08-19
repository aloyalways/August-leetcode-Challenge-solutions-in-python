class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if (K==0 and N==1) or N==1:
            ans=[0]
        else:
            ans=[]
        def helper(n,number):
            if n==N-1:
                ans.append(number)
                return
            if (number%10)-K>=0:
                helper(n+1,number*10+((number%10)-K))
            if (number%10)+K<=9:
                helper(n+1,number*10+((number%10)+K))
        
        for i in range(1,10):
            helper(0,i)
        return set(ans)

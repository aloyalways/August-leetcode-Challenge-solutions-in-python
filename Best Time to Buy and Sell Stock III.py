class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        def solve(i,bought,count):
            if i==len(prices)-1:
                if bought:
                    return prices[i]
                else:
                    return 0
            if dp[i][bought][count]!=-1:
                return dp[i][bought][count]
            if bought:
                dp[i][bought][count]=max(solve(i+1,bought,count),prices[i]+solve(i+1,False,count))
                return dp[i][bought][count]
            else:
                if count>0:
                    dp[i][bought][count]=max(solve(i+1,bought,count),solve(i+1,True,count-1)-prices[i])
                else:
                    dp[i][bought][count]=solve(len(prices)-1,bought,count)
                return dp[i][bought][count]
        
        dp=[[[-1]*3 for i in range(2)] for j in range(len(prices))]
        return solve(0,False,2)

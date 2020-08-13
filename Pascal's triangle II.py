class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        if rowIndex==1:
            return [1]
        i=2
        ans=[[1]]
        while i<=rowIndex:
            ans.append([0]*i)
            ans[1][0],ans[1][-1]=1,1
            for j in range(1,i-1):
                ans[1][j]=ans[0][j-1]+ans[0][j]
            ans.pop(0)
            i+=1
        return ans[0]

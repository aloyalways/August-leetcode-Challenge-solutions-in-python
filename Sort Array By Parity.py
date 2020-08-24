class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i,j=0,len(A)-1
        while i<=j:
            if A[i]%2==0 and A[j]%2!=0:
                i+=1
                j-=1
            elif A[i]%2==0:
                i+=1
            elif A[j]%2!=0:
                j-=1
            else:
                A[i],A[j]=A[j],A[i]
                i+=1
                j-=1
        return A

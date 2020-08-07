class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            n=abs(i)
            if nums[n-1]<0:
                ans.append(n)
            else:
                nums[n-1]*=-1
        return ans

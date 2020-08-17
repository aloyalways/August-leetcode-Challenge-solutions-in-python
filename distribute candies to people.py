class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n=1
        ans=[0]*num_people
        while candies>=0:
            i=0 
            while i<num_people:
                if candies-n<0:
                    ans[i]+=candies
                    candies-=n
                    break
                ans[i]+=n
                candies-=n
                n+=1
                i+=1
        return ans

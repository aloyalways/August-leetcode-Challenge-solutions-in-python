from collections import defaultdict
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startPoint=defaultdict(list)
        for i in range(len(intervals)):
            startPoint[intervals[i][0]].append(i)

        maxRange=max(startPoint)
        ans=[]
        for i in intervals:
            for j in range(i[1],maxRange+1):
                if j in startPoint:
                    ans.append(startPoint[j][0])
                    break
            else:
                ans.append(-1)
        return ans

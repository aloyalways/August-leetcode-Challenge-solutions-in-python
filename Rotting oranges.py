class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x=len(grid)
        y=len(grid[0])
        fresh=0
        for i in range(x):
            for j in range(y):
                if grid[i][j]==1:
                    fresh+=1
        minutes=0
        prev=fresh
        while True:
            cp=copy.deepcopy(grid)
            for i in range(x):
                for j in range(y):
                    if grid[i][j]==2:
                        for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                            if 0<=r<x and 0<=c<y and cp[r][c]==1:
                                cp[r][c]=2
                                fresh-=1
            if prev==fresh:
                break
            prev=fresh
            minutes+=1
            grid=cp
        if fresh>0:
            return -1
        return minutes

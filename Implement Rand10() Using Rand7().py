# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def __init__(self):
        self.arr=[[0 for _ in range(7)] for _ in range(7)]
        n=1
        for r in range(7):
            for c in range(7):
                self.arr[r][c]=(n-1)%10+1
                n+=1
                
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row=rand7()-1
            col=rand7()-1
            if row==6 or row==5 and col>=5:
                continue
            return self.arr[row][col]
        

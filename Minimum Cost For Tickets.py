from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def helper(day):
            if day>days[-1]:
                return 0
            if day in days:
                return min(costs[0]+helper(day+1),costs[1]+helper(day+7),costs[2]+helper(day+30))
            else:
                return helper(day+1)
            
        return helper(days[0])

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # greedy 
        # i moves right if i + 1 is taller 
        # j moves left if j - 1 is shorter 
        # else move both 
        i = 0 
        j = len(heights) - 1 
        res = min(heights[i],heights[j])*(j-i)
        while i < j: 
            if heights[j] > heights[i]:
                i += 1 
            elif heights[i] > heights[j]:
                j -= 1 
            else: 
                i += 1 
                j -= 1 
            temp = min(heights[i],heights[j])*(j-i)
            res = max(temp, res)
        return res 
            
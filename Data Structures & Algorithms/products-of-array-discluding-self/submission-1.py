class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # all to left of i 
        # left 1 1 2 8
        # all to right of i 
        leftarr = [1] * len(nums)
        rightarr = [1] * len(nums)
        for i in range(1, len(nums)):
            leftarr[i] = leftarr[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1): 
            # 48 24 6 1
            # i = 0
            rightarr[i] = rightarr[i+1] * nums[i+1]
        
        res = []
        # 48 24 12 8
        for i in range(len(nums)):
            res.append(leftarr[i]*rightarr[i])
        return res 

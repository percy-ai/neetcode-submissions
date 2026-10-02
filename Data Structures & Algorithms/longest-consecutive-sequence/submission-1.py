class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set 
        # start of sequence if nums-1 not in set -> start constructing and removing them from set 
        if not nums:
            return 0 
        comp = set(nums)
        temp = 1
        res = 1 

        for num in nums: 
            temp = 1
            if num - 1 in comp:
                continue 
            while num + 1 in comp: # 3
                comp.remove(num+1)
                num += 1 
                temp += 1 # temp = 2 
            res = max(temp, res)
        return res
        # end of sequence if nums+1 not in set 

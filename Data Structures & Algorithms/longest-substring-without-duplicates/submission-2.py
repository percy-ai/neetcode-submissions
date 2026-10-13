class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # increment window if all chars are unique 
        # unique if we add new right char and the count < 1 
        if len(s) <= 1:
            return len(s)
        left = 0 
        hm = defaultdict(int)
        res = 0 
        for right in range(len(s)): 
            hm[s[right]] += 1 
            while hm[s[right]] > 1:
                hm[s[left]] -= 1 
                if hm[s[left]] == 0:
                    del hm[s[left]]
                left += 1 
            right += 1 
            res = max(res, right-left)
        return res 
                

            
        # else decrement window from left until chars are unique again 
            # decrement the right count, check and rm if it == 0 
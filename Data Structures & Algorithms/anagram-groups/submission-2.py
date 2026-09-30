class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {"a":1,"c":1,"t:1"}: [act, cat]
        res = {} # {{a:1,c:1,t:1}:[act], {p:1,o:1,t:1,s:1}:[pots, tops]}, 
        for s in strs:
            hm = frozenset(Counter(s).items()) # {t:1,o:1,p:1,s:1}
            if  not hm in res:
                res[hm] = [s]
            else:
                res[hm].append(s)
        return list(res.values())

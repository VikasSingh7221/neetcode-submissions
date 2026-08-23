class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        for i in t:
            if i in dic.keys():
                dic[i]-=1
        return not any(dic.values())
        
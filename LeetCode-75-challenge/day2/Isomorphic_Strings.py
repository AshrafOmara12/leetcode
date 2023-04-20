# problem link: https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_map = []
            t_map = []
            for letter in s:
                s_map.append(s.index(letter))
            for letter in t:
                t_map.append(t.index(letter))
            if s_map == t_map:
                return True
            return False
        return False
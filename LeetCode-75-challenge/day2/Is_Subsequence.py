# problem link: https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ele = ''
        i = 0
        for j in range(len(t)):
            if i <= len(s) -1:
                if s[i] == t[j]:
                    ele += t[j]
                    i += 1
        if ele == s:
            return True
        else:
            return False

#Another Solution
t = 'ahbgdc'
s = 'axc'
i, j = 0, 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1
print(i == len(s))
# problem link: https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

s = "badc"
t = "baba"
check = set()
for ele in zip(list(s), list(t)):
    print(ele)
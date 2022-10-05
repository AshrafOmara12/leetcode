import collections


strs = ["eat","tea","tan","ate","nat","bat"]
ans = collections.defaultdict(list)
# print(ans)
for s in strs:
    # ans[tuple(sorted(s))].append(s)
    ans[tuple(sorted(s))].append(s)
print(ans.values())
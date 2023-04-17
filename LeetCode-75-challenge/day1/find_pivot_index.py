# problem link: https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
class Solution:
    def pivot_index(self, nums: list[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0
        total = 0
        for i in range(len(nums)):
            if i > 0:
                previous = total
                current = nums[i-1]
                total = current + previous
                if total == sum(nums[i+1:]):
                    return i
        return -1
obj = Solution()
obj.pivot_index([1,7,3,6,5,6])




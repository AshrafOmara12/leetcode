# problem link: https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

# answer
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sums = []
        for i in range(len(nums)):
            if len(sums) == 0:
                sums.append(nums[i])
            else:
                current = nums[i]
                previous = sums[i-1]
                print(current, previous)
                total = current + previous
                sums.append(total) 
        return sums
__author__ = 'Ashraf'

nums = [2,3,2]
target = 4
#
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[j] == target - nums[i]:
#             print([i, j])
#         else:
#             continue


data = {}

for i in range(len(nums)):
    data[i] = nums[i]

for i in range(len(nums)):
    num = target - nums[i]
    if num in data and data[num] != i:
        print([i, data[num]])
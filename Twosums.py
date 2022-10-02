def indices(list, item):
    return [i for i, x in enumerate(list) if x == item]

def twoSum(nums, target):
    from itertools import combinations

    com = combinations(nums,2)
    for i in com:
        if sum(i) == target:
            if i[0] == i[1]:
                print( indices(nums,i[0]))
            else:
                print (nums.index(i[0]),nums.index(i[1]))
        else:
            continue


twoSum([4,2,4],8)
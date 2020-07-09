# Two sum:

def two_sum(nums, target):
    for i in range(len(nums)):
        solution = target - nums[i]
        if solution in nums and nums.index(solution) != i:
            return [i, nums.index(solution)]

sum_array = [2,4,6,8,1,3,5]

# test cases:
assert(two_sum(sum_array, 14)) == [2,3]
assert(two_sum(sum_array, 17)) == None

# -------------------------------------------------------
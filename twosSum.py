import math

###
# NOTE: For the ThreesSum problem, just iterate through the list, and for each element call TwosSum. O(n^2)
# So say we're on a certain element, get the difference between current value and the target. Then Call TwosSum on the difference.
# Because we're looking for some pair that equals the difference we need, and that will give us the 3 values that equal the target.
# Then just append our index to the returned indices returned from TwosSum.
# Will need to do some extra to avoid duplicates. For example, the array provided to TwosSum should exclude the index we're on. We should
# also skip any same values in our array, so sort and skip sames, or create hash and iterate keys.
#
# Algorithms
# Using two pointer system
# N log N + N / 2
#
# Hash
# 2N
#
# If N = 64, the two ptr system gives us 480 and the hash system gives us 128. Hash is WAY faster.
# If being called for 3 sum, so an extra N multiplied to the entire equation, the two ptr system gives us 30,720 and hash gives 8192.
# So has is WAY faster, but at the cost of fairly significant memory.
###

###
# Find all pair values who's sum is the target. Return indices of all pairs.
###

# Sort and use two pointers to scan for pairs. n log n + n / 2 (sort + scan) -- O(n)


def twoSumTwoPointer(nums, targetValue):
    pairs = []
    startIdx = 0
    endIdx = len(nums) - 1
    nums = sorted(nums)

    while startIdx < endIdx:
        sum = nums[startIdx] + nums[endIdx]
        if sum is targetValue:
            pairs.append([startIdx, endIdx])
            startIdx += 1
            endIdx -= 1
        elif sum < targetValue:
            # NOTE: If we were skipping duplicates, since this is sorted, I could just continue to increment while value is the same.
            startIdx += 1
        elif sum > targetValue:
            endIdx -= 1

    return pairs

# Store all values with index in hash. Scan for missing difference needed to equal sum. n + n (create lookup + scan) O(n)


def twoSumHash(nums, targetValue):
    lookup = {}
    pairs = []

    for i in range(len(nums)):
        lookup[nums[i]] = i

    for i in range(len(nums)):
        diff = targetValue - nums[i]
        if diff in lookup:
            pairs.append([i, lookup[diff]])

            del lookup[diff]  # Avoid duplicates ((0, 4), (4, 0))
            if nums[i] in lookup:
                del lookup[nums[i]]

    return pairs

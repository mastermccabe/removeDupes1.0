# Given an array of integers, find out whether there
# are two \
# distinct indices i and j in the array such that the
#  absolute difference between nums[i] and nums[j] is
#  at most t and the absolute difference
#  between i and j is at most k

# @param {integer[]} nums
# @param {integer} k
# @param {integer} t
# @return {boolean}
def containsNearbyAlmostDuplicate(nums, k, t):
    ind = sorted(range(len(nums)), key = lambda x: nums[x])
    for i in range(len(nums)-1):
        j = i + 1
        while j < len(nums) and nums[ind[j]] - nums[ind[i]] <= t:
            if abs(ind[i]-ind[j]) <= k:
                return True
            j += 1
    return False
